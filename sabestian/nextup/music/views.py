from django.shortcuts import render
from authentication.models import userDetails 
from music.models import song
from django.http import HttpResponse,Http404
import json

# Create your views here.

def likeSong(request):
	songName = request.POST.get("songName")
	artistName = request.POST.get("artistName")
	print(songName, artistName)
	userDetailsObj = userDetails.objects.filter(userHandle = artistName)
	if (len(userDetailsObj) == 0):
		status = 0
		message = "Artist does not exist !"
	else:
		userDetailsObj = userDetailsObj[0]
		songObj = song.objects.filter(artist = userDetailsObj, songName = songName)
		if (len(songObj) == 0):
			status = 0
			message = "Song for this artist does not exist !"
		else:
			songObj = songObj[0]
			songObj.numberOfLikes += 1
			print(songObj)
			songObj.save()
			status = 1
			message = "Song liked !"
	return HttpResponse(
		json.dumps(
			{
				"status": status,
				"message": message
			}), content_type="application/json")
	
