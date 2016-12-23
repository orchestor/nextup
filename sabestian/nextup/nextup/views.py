from django.shortcuts import render
from django.template.context import RequestContext
from music.models import song

# Create your views here.

# Rendering of home page.
def home(request):
	if (request.user.is_authenticated()):
		displayPage = "user-profile-page.html"
		songs = song.objects.filter()
		print(songs[0].songName)
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
		return render(request, displayPage, {
			'songs': responseArr,
			'topSong': responseArr[-1]["songName"],
			'topArtist': responseArr[-1]["artistName"],
			'topLikes': responseArr[-1]["numberOfLikes"]
		})
	else:
		displayPage = "user-login.html"

	return render(request, displayPage)

def successSignup(request):
	return render(request, "success-signup.html")