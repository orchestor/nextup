from django.shortcuts import render
from utility_constants import *
from django.http import HttpResponse, Http404
import json
import base64
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from authentication.models import userDetails, follow
from music.models import likedSongs, song
from django.conf import settings

# Create your views here.

# Login functionality for both artist and listener. Called through an Ajax request.
# Parameters in request - email and password
def login(request):
	email = request.POST.get(EMAIL_KEY)
	password = request.POST.get(PASSWORD_KEY)
	print(email, password)
	message = EMPTY_STRING
	# Gives status of request -> 1 is success and 0 is error
	status = 0

	try:
		user = auth.authenticate(username = email, password = password)
	except Exception, e:
		message = GENERAL_ERROR_MESSAGE
		status = 0
	else:
		if (user is not None):
			if (user.is_active):
				auth.login(request, user)
				message = SUCCESSFUL_LOGIN_MESSAGE
				status = 1
			else:
				message = UNAUTHORIZED_LOGIN_MESSAGE
				status = 0
		else:
			message = AUTHENTICATION_ERROR_MESSAGE
			status = 0
	return HttpResponse(
		json.dumps(
			{
				"status": status,
				"message": message
			}), content_type="application/json")

#Function to logout a user.
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def createUser(firstName, email, password):
	user = User.objects.create(
		username = email, first_name = firstName, 
		is_active = False, email = email
	);
	user.set_password(password)
	user.save()
	return user

def emailIsUnique(email):
	user = User.objects.filter(username = email)
	if (len(user) > 0):
		return False
	return True

def firstNameIsValid(firstName):
	if (len(firstName) == 0):
		return False
	return True

def passwordIsValid(password):
	if (len(password) < 6):
		return False
	return True

def userHandleIsUnique(userHandle):
	userDetailsObject = userDetails.objects.filter(userHandle = userHandle)
	if (len(userDetailsObject) > 0):
		return False
	return True

def registerUserHelper(request):
	firstName = request.POST.get('firstName')
	email = request.POST.get('email')
	password = request.POST.get('password')
	userHandle = request.POST.get('userHandle')
	age = request.POST.get('age')
	gender = request.POST.get('gender')
	type = request.POST.get('type')
	areaCode = request.POST.get('areaCode')

	print(firstName, email, password)
	if (emailIsUnique(email)):
		if (firstNameIsValid(firstName)):
			if (passwordIsValid(password)):
				if (userHandleIsUnique(userHandle)):
					user = createUser(firstName, email, password)
					userDetails.objects.create(
						user = user,
						userHandle = userHandle,
						age = age,
						gender = gender,
						type = type,
						areaCode = areaCode
					)
					encoded = base64.b64encode(email, "utf-8")
					encoded = encoded.decode("utf-8")
					accountVerificationLink = settings.DOMAIN_NAME + "/verify-user-account?user=" + encoded
					email = EmailMessage('Account Verification Request || Napollo', accountVerificationLink, to=[email])
					# email.send()
					# sendMail(email, settings.SENDGRID_SENDFROM, "Account Verification Request || Decora Systems", accountVerificationLink)
					message = "Account creation successfull !"
					status = 0
				else:
					message = "User handle is preoccupied !"
					status = 4
			else:
				message = "Password is less than 6 characters in length !"
				status = 1
		else:
			message = "First Name cannot be empty !"
			status = 2
	else:
		message = "This email already exists !"
		status = 3
	return {
		"message": message,
		"status": status
	}	

#Function for signup of new user to website. Called through an Ajax request.
def signup(request):
	responseObject = registerUserHelper(request)
	return HttpResponse(
		json.dumps(
			{
				"status": responseObject["status"],
				"message": responseObject["message"]
			}), content_type="application/json")

def checkUserhandle(request):
	userHandle = request.GET.get('userHandle')
	if (userHandle == ""):
		message = "User handle cannot be blank !"
		status = 0
	else:
		if (not userHandleIsUnique(userHandle)):
			message = "This user handle is preoccupied !"
			status = 0
		else:
			message = "User handle is available."
			status = 1
	return HttpResponse(
		json.dumps(
			{
				"status": status,
				"message": message
			}), content_type="application/json")

def userProfile(request):
	if (request.user):
		if (request.user.is_authenticated()):
			userHandle = request.GET.get("userHandle")
			userDetailsObject = userDetails.objects.filter(userHandle = userHandle)
			if (len(userDetailsObject) > 0):
				userDetailsObject = userDetailsObject[0]
				user = userDetailsObject.user
				temp = {
					"userHandle": userDetailsObject.userHandle
				}
				if (userDetailsObject.profilePicture):
					temp["profilePicture"] = userDetailsObject.profilePicture.url
				else:
					temp["profilePicture"] = ""
				followObject = follow.objects.filter(follower = request.user, following = user)
				if (len(followObject) > 0):
					temp["isFollowing"] = True
				else:
					temp["isFollowing"] = False
				temp["likedSongsArr"] = likedSongs.objects.filter(user = userDetailsObject)
				temp["numberOfLikedSongs"] = len(temp["likedSongsArr"])
				temp["numberOfFollowers"] = len(follow.objects.filter(following = user))
				temp["numberOfFollowing"] = len(follow.objects.filter(follower = user))
				if (userDetailsObject.type == "Artist"):
					temp["uploadedSongsArr"] = song.objects.filter(artist = userDetailsObject)
				print(temp)
				return render(request, "user-profile-page.html", {"data": temp})
	else:
		raise Http404

def follow_user(request):
	userHandle = request.GET.get("userHandle")
	userDetailsObject = userDetails.objects.filter(userHandle = userHandle)
	if (len(userDetailsObject) > 0):
		userDetailsObject = userDetailsObject[0]
		followObject = follow.objects.filter(follower = request.user, following = userDetailsObject.user)
		if (len(followObject) > 0):
			pass
		else:
			follow.objects.create(follower = request.user, following = userDetailsObject.user)
		return HttpResponse(
			json.dumps(
				{
					"status": 1,
					"message": "User followed"
				}), content_type="application/json")

def unfollow_user(request):
	userHandle = request.GET.get("userHandle")
	userDetailsObject = userDetails.objects.filter(userHandle = userHandle)
	if (len(userDetailsObject) > 0):
		userDetailsObject = userDetailsObject[0]
		followObject = follow.objects.filter(follower = request.user, following = userDetailsObject.user)
		if (len(followObject) > 0):
			followObject[0].delete()
		else:
			pass
		return HttpResponse(
			json.dumps(
				{
					"status": 1,
					"message": "User unfollowed"
				}), content_type="application/json")
