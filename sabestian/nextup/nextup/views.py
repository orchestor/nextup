from django.shortcuts import render
from django.template.context import RequestContext
from music.models import song, likedSongs
from authentication.models import userDetails

# Create your views here.

# Rendering of home page.
def home(request):
	if (request.user.is_authenticated()):
		displayPage = "user-profile-page.html"
		if (request.GET.get("genre") == "pop"):
			songs = song.objects.filter(genre = "Latin Pop")
		elif (request.GET.get("genre") == "rock"):
			songs = song.objects.filter(genre = "Rock/Oldies")
		elif (request.GET.get("genre") == "hiphop"):
			songs = song.objects.filter(genre = "Hip-Hop")
		elif (request.GET.get("genre") == "country"):
			songs = song.objects.filter(genre = "Country")
		else:
			songs = song.objects.filter()
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
	return render(request, "expansion.html")

def northWest(request):
	return render(request, "north-west.html")

def southWest(request):
	return render(request, "south-west.html")

def northCentral(request):
	return render(request, "north-central.html")

def southCentral(request):
	return render(request, "south-central.html")

def northEast(request):
	return render(request, "north-east.html")

def southEast(request):
	return render(request, "south-east.html")

def alabama(request):
	return render(request, 'alabama.html')

def alaska(request):
	return render(request, 'alaska.html')

def arizona(request):
	return render(request, 'arizona.html')

def arkansas(request):
	return render(request, 'arkansas.html')

def california(request):
	return render(request, 'california.html')

def colorado(request):
	return render(request, 'colorado.html')

def connecticut(request):
	return render(request, 'connecticut.html')

def delaware(request):
	return render(request, 'delaware.html')

def districtofColumbia(request):
	return render(request, 'districtofColumbia.html')

def florida(request):
	return render(request, 'florida.html')

def georgia(request):
	return render(request, 'georgia.html')

def hawaii(request):
	return render(request, 'hawaii.html')

def idaho(request):
	return render(request, 'idaho.html')

def illinois(request):
	return render(request, 'illinois.html')

def indiana(request):
	return render(request, 'indiana.html')

def iowa(request):
	return render(request, 'iowa.html')

def kansas(request):
	return render(request, 'kansas.html')

def kentucky(request):
	return render(request, 'kentucky.html')

def louisiana(request):
	return render(request, 'louisiana.html')

def maine(request):
	return render(request, 'maine.html')

def maryland(request):
	return render(request, 'maryland.html')

def massachusetts(request):
	return render(request, 'massachusetts.html')

def michigan(request):
	return render(request, 'michigan.html')

def minnesota(request):
	return render(request, 'minnesota.html')

def mississippi(request):
	return render(request, 'mississippi.html')

def missouri(request):
	return render(request, 'missouri.html')

def montana(request):
	return render(request, 'montana.html')

def nebraska(request):
	return render(request, 'nebraska.html')

def nevada(request):
	return render(request, 'nevada.html')

def newHampshire(request):
	return render(request, 'newHampshire.html')

def newJersey(request):
	return render(request, 'newJersey.html')

def newMexico(request):
	return render(request, 'newMexico.html')

def newYork(request):
	return render(request, 'newYork.html')

def northCarolina(request):
	return render(request, 'northCarolina.html')

def northDakota(request):
	return render(request, 'northDakota.html')

def ohio(request):
	return render(request, 'ohio.html')

def oklahoma(request):
	return render(request, 'oklahoma.html')

def oregon(request):
	return render(request, 'oregon.html')

def pennsylvania(request):
	return render(request, 'pennsylvania.html')

def rhodeIsland(request):
	return render(request, 'rhodeIsland.html')

def southCarolina(request):
	return render(request, 'southCarolina.html')

def southDakota(request):
	return render(request, 'southDakota.html')

def tennessee(request):
	return render(request, 'tennessee.html')

def texas(request):
	return render(request, 'texas.html')

def utah(request):
	return render(request, 'utah.html')

def vermont(request):
	return render(request, 'vermont.html')

def virginia(request):
	return render(request, 'virginia.html')

def washington(request):
	return render(request, 'washington.html')

def westVirginia(request):
	return render(request, 'westVirginia.html')

def wisconsin(request):
	return render(request, 'wisconsin.html')

def wyoming(request):
	return render(request, 'wyoming.html')