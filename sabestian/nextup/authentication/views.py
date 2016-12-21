from django.shortcuts import render
from utility_constants import *
from django.http import HttpResponse,Http404
import json
from django.contrib import auth

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
		print(e)
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
