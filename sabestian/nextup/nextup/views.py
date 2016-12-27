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

def alabamaR1(request):
	return render(request, 'alabamaR1.html')

def alabamaR2(request):
	return render(request, 'alabamaR2.html')

def alaska(request):
	return render(request, 'alaska.html')

def arizona(request):
	return render(request, 'arizona.html')

def arizonaR1(request):
	return render(request, 'arizonaR1.html')

def arizonaR2(request):
	return render(request, 'arizonaR2.html')

def arkansas(request):
	return render(request, 'arkansas.html')

def arkansasR1(request):
	return render(request, 'arkansasR1.html')

def arkansasR2(request):
	return render(request, 'arkansasR2.html')

def california(request):
	return render(request, 'california.html')

def californiaR1(request):
	return render(request, 'californiaR1.html')

def californiaR2(request):
	return render(request, 'californiaR2.html')

def californiaR3(request):
	return render(request, 'californiaR3.html')

def colorado(request):
	return render(request, 'colorado.html')

def coloradoR1(request):
	return render(request, 'coloradoR1.html')

def coloradoR2(request):
	return render(request, 'coloradoR2.html')

def connecticut(request):
	return render(request, 'connecticut.html')

def delaware(request):
	return render(request, 'delaware.html')

def districtofColumbia(request):
	return render(request, 'districtofColumbia.html')

def florida(request):
	return render(request, 'florida.html')

def floridaR1(request):
	return render(request, 'floridaR1.html')

def floridaR2(request):
	return render(request, 'floridaR2.html')

def floridaR3(request):
	return render(request, 'floridaR3.html')

def georgia(request):
	return render(request, 'georgia.html')

def georgiaR1(request):
	return render(request, 'georgiaR1.html')

def georgiaR2(request):
	return render(request, 'georgiaR2.html')

def hawaii(request):
	return render(request, 'hawaii.html')

def idaho(request):
	return render(request, 'idaho.html')

def idahoR1(request):
	return render(request, 'idahoR1.html')

def idahoR2(request):
	return render(request, 'idahoR2.html')

def idahoR3(request):
	return render(request, 'idahoR3.html')

def illinois(request):
	return render(request, 'illinois.html')

def indiana(request):
	return render(request, 'indiana.html')

def iowa(request):
	return render(request, 'iowa.html')

def iowaR1(request):
	return render(request, 'iowaR1.html')

def iowaR2(request):
	return render(request, 'iowaR2.html')

def iowaR3(request):
	return render(request, 'iowaR3.html')

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

def massachusettsR1(request):
	return render(request, 'massachusettsR1.html')

def massachusettsR2(request):
	return render(request, 'massachusettsR2.html')

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

def newYorkR1(request):
	return render(request, 'newYorkR1.html')

def newYorkR2(request):
	return render(request, 'newYorkR2.html')

def newYorkR3(request):
	return render(request, 'newYorkR3.html')

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

def texasR1(request):
	return render(request, 'texasR1.html')

def texasR2(request):
	return render(request, 'texasR2.html')

def texasR3(request):
	return render(request, 'texasR3.html')

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