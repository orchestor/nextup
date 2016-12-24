from django.shortcuts import render
from django.template.context import RequestContext
from music.models import song, likedSongs
from authentication.models import userDetails

# Create your views here.

# Rendering of home page.
def home(request):
	if (request.user.is_authenticated()):
		displayPage = "user-profile-page.html"
		if (request.GET.get("genre") == "all"):
			songs = song.objects.filter()
		elif (request.GET.get("genre") == "pop"):
			songs = song.objects.filter(genre = "Latin Pop")
		elif (request.GET.get("genre") == "rock"):
			songs = song.objects.filter(genre = "Rock/Oldies")
		elif (request.GET.get("genre") == "hiphop"):
			songs = song.objects.filter(genre = "Hip-Hop")
		elif (request.GET.get("genre") == "country"):
			songs = song.objects.filter(genre = "Country")
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