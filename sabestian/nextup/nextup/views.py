from django.shortcuts import render
from django.template.context import RequestContext
from music.models import song, likedSongs
from authentication.models import userDetails

# Create your views here.

# Rendering of home page.
def home(request):
	if (request.user.is_authenticated()):
		displayPage = "home.html"
		if (request.GET.get("genre") == "pop"):
			songs = song.objects.filter(genre = "Latin Pop", status = "Complete")
		elif (request.GET.get("genre") == "rock"):
			songs = song.objects.filter(genre = "Rock/Oldies", status = "Complete")
		elif (request.GET.get("genre") == "hiphop"):
			songs = song.objects.filter(genre = "Hip-Hop", status = "Complete")
		elif (request.GET.get("genre") == "country"):
			songs = song.objects.filter(genre = "Country", status = "Complete")
		else:
			songs = song.objects.filter(status = "Complete")
		# print(songs[0].songName)
		responseArr = []
		for s in songs:
			temp = {}
			temp["songName"] = s.songName
			temp["artistName"] = s.artist.userHandle
			temp["cover"] = s.coverPic.url
			if (s.songFile != ""):
				temp["songFile"] = s.songFile.url
			else:
				temp["songFile"] = s.songFile
			temp["numberOfLikes"] = s.numberOfLikes
			responseArr.append(temp)
		print(responseArr)
		alsoLikedSongArr = []
		print(request.user)
		userHandle = userDetails.objects.filter(user = request.user)
		if (len(userHandle) > 0):
			userHandle = userHandle[0]
		print(userHandle)
		alsoLiked = likedSongs.objects.filter(user = userHandle)
		print(alsoLiked)
		for a in alsoLiked:
			likedS = a.song
			temp = {}
			temp["songName"] = likedS.songName
			temp["artistName"] = likedS.artist.userHandle
			temp["cover"] = likedS.coverPic.url
			if (likedS.songFile != ""):
				temp["songFile"] = likedS.songFile.url
			else:
				temp["songFile"] = likedS.songFile
			temp["numberOfLikes"] = likedS.numberOfLikes
			alsoLikedSongArr.append(temp)
		print(alsoLikedSongArr)
		if (len(responseArr) > 0):
			return render(request, displayPage, {
				'songs': responseArr,
				'topSong': responseArr[-1]["songName"],
				'topArtist': responseArr[-1]["artistName"],
				'topLikes': responseArr[-1]["numberOfLikes"],
				'topCover': responseArr[-1]["cover"],
				'alsoLiked': alsoLikedSongArr
			})
		else:
			return render(request, displayPage, {
				'songs': responseArr,
				'topSong': "",
				'topArtist': "",
				'topLikes': "",
				'topCover': "",
				'alsoLiked': alsoLikedSongArr
			})			
	else:
		displayPage = "user-login.html"

	return render(request, displayPage)

def successSignup(request):
	return render(request, "success-signup.html")

def expansion(request):
	userDetailsArr = userDetails.objects.filter()
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	print(finalArr)
	return render(request, "expansion.html", {"data": finalArr})

def northWest(request):
	userDetailsArr = userDetails.objects.filter(areaCode__division = "NorthWestern")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, "north-west.html", {"data": finalArr})

def southWest(request):
	userDetailsArr = userDetails.objects.filter(areaCode__division = "SouthWestern")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, "south-west.html", {"data": finalArr})

def northCentral(request):
	userDetailsArr = userDetails.objects.filter(areaCode__division = "NorthCentral")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, "north-central.html", {"data": finalArr})

def southCentral(request):
	userDetailsArr = userDetails.objects.filter(areaCode__division = "SouthCentral")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, "south-central.html", {"data": finalArr})

def northEast(request):
	userDetailsArr = userDetails.objects.filter(areaCode__division = "NorthEastern")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, "north-east.html", {"data": finalArr})

def southEast(request):
	userDetailsArr = userDetails.objects.filter(areaCode__division = "SouthEastern")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, "south-east.html", {"data": finalArr})

def alabama(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Alabama")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, 'alabama.html', {"data": finalArr})

def alabamaR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Alabama", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, 'alabamaR1.html', {"data": finalArr})

def alabamaR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Alabama", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)
	return render(request, 'alabamaR2.html', {"data": finalArr})

def alaska(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Alaska")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'alaska.html', {"data": finalArr})

def arizona(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Arizona")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'arizona.html', {"data": finalArr})

def arizonaR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Arizona", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'arizonaR1.html', {"data": finalArr})

def arizonaR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Arizona", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'arizonaR2.html', {"data": finalArr})

def arkansas(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Arkansas")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'arkansas.html', {"data": finalArr})

def arkansasR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Arkansas", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'arkansasR1.html', {"data": finalArr})

def arkansasR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Arkansas", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'arkansasR2.html', {"data": finalArr})

def california(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "California")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'california.html', {"data": finalArr})

def californiaR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "California", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'californiaR1.html', {"data": finalArr})

def californiaR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "California", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'californiaR2.html', {"data": finalArr})

def californiaR3(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "California", areaCode__region = 3)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'californiaR3.html', {"data": finalArr})

def colorado(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Colarodo")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'colorado.html', {"data": finalArr})

def coloradoR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Colarodo", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'coloradoR1.html', {"data": finalArr})

def coloradoR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Colarodo", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'coloradoR2.html', {"data": finalArr})

def connecticut(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Connecticut")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'connecticut.html', {"data": finalArr})

def delaware(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Delaware")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'delaware.html', {"data": finalArr})

def districtofColumbia(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "District Of Columbia")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'districtofColumbia.html', {"data": finalArr})

def florida(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Florida")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'florida.html', {"data": finalArr})

def floridaR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Florida", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'floridaR1.html', {"data": finalArr})

def floridaR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Florida", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'floridaR2.html', {"data": finalArr})

def floridaR3(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Florida", areaCode__region = 3)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'floridaR3.html', {"data": finalArr})

def georgia(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Georgia")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'georgia.html', {"data": finalArr})

def georgiaR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Georgia", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'georgiaR1.html', {"data": finalArr})

def georgiaR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Georgia", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'georgiaR2.html', {"data": finalArr})

def hawaii(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Hawaii")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'hawaii.html', {"data": finalArr})

def idaho(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Idaho")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'idaho.html', {"data": finalArr})

def idahoR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Idaho", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'idahoR1.html', {"data": finalArr})

def idahoR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Idaho", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'idahoR2.html', {"data": finalArr})

def idahoR3(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Idaho", areaCode__region = 3)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'idahoR3.html', {"data": finalArr})

def illinois(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Illinois")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'illinois.html', {"data": finalArr})

def indiana(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Indiana")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'indiana.html', {"data": finalArr})

def iowa(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Iowa")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'iowa.html', {"data": finalArr})

def iowaR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Iowa", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'iowaR1.html', {"data": finalArr})

def iowaR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Iowa", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'iowaR2.html', {"data": finalArr})

def iowaR3(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Iowa", areaCode__region = 3)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'iowaR3.html', {"data": finalArr})

def kansas(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Kansas")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'kansas.html', {"data": finalArr})

def kentucky(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Kentucky")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'kentucky.html', {"data": finalArr})

def louisiana(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Lousiana")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'louisiana.html', {"data": finalArr})

def maine(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Maine")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'maine.html', {"data": finalArr})

def maryland(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Maryland")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'maryland.html', {"data": finalArr})

def massachusetts(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Massachusetts")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'massachusetts.html', {"data": finalArr})

def massachusettsR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Massachusetts", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'massachusettsR1.html', {"data": finalArr})

def massachusettsR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Massachusetts", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'massachusettsR2.html', {"data": finalArr})

def michigan(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Michigan")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'michigan.html', {"data": finalArr})

def minnesota(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Minnessota")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'minnesota.html', {"data": finalArr})

def mississippi(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Mississipi")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'mississippi.html', {"data": finalArr})

def missouri(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Missouri")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'missouri.html', {"data": finalArr})

def montana(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Montana")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'montana.html', {"data": finalArr})

def nebraska(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Nebraska")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'nebraska.html', {"data": finalArr})

def nevada(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Nevada")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'nevada.html', {"data": finalArr})

def newHampshire(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New Hampshire")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newHampshire.html', {"data": finalArr})

def newJersey(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New Jersey")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newJersey.html', {"data": finalArr})

def newMexico(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New Mexico")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newMexico.html', {"data": finalArr})

def newYork(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New York")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newYork.html', {"data": finalArr})

def newYorkR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New York", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newYorkR1.html', {"data": finalArr})

def newYorkR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New York", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newYorkR2.html', {"data": finalArr})

def newYorkR3(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "New York", areaCode__region = 3)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'newYorkR3.html', {"data": finalArr})

def northCarolina(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "North Carolina")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'northCarolina.html', {"data": finalArr})

def northDakota(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "North Dakota")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'northDakota.html', {"data": finalArr})

def ohio(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Ohio")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'ohio.html', {"data": finalArr})

def oklahoma(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Oklahoma")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'oklahoma.html', {"data": finalArr})

def oregon(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Oregon")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'oregon.html', {"data": finalArr})

def pennsylvania(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Pennslyvania")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'pennsylvania.html', {"data": finalArr})

def rhodeIsland(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Rhode Island")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'rhodeIsland.html', {"data": finalArr})

def southCarolina(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "South Carolina")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'southCarolina.html', {"data": finalArr})

def southDakota(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "South Dakota")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'southDakota.html', {"data": finalArr})

def tennessee(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Tennessee")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'tennessee.html', {"data": finalArr})

def texas(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Texas")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'texas.html', {"data": finalArr})

def texasR1(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Texas", areaCode__region = 1)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'texasR1.html', {"data": finalArr})

def texasR2(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Texas", areaCode__region = 2)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'texasR2.html', {"data": finalArr})

def texasR3(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Texas", areaCode__region = 3)
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'texasR3.html', {"data": finalArr})

def utah(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Utah")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'utah.html', {"data": finalArr})

def vermont(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Vermont")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'vermont.html', {"data": finalArr})

def virginia(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Virginia")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'virginia.html', {"data": finalArr})

def washington(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Washington")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'washington.html', {"data": finalArr})

def westVirginia(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "West Virginia")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'westVirginia.html', {"data": finalArr})

def wisconsin(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Wisconsin")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'wisconsin.html', {"data": finalArr})

def wyoming(request):
	userDetailsArr = userDetails.objects.filter(areaCode__state = "Wyoming")
	finalArr = []
	for u in userDetailsArr:
		temp = {
			"userHandle": u.userHandle,
			"profilePic": u.profilePicture.url
		}
		songArr = song.objects.filter(artist = u)
		cummulative = 0
		for s in songArr:
			cummulative += s.numberOfLikes
		temp["numberOfLikes"] = cummulative
		finalArr.append(temp)
		finalArr.sort(key=lambda x: x["numberOfLikes"], reverse=True)

	return render(request, 'wyoming.html', {"data": finalArr})