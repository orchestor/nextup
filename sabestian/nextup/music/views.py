from django.shortcuts import render
from authentication.models import userDetails 
from music.models import *
from django.http import HttpResponse,Http404
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
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
			isAlreadyLiked = likedSongs.objects.filter(song = songObj, user = userDetailsObj)
			if (len(isAlreadyLiked) > 0):
				status = 1
				message = "Song Already liked !"
			else:
				likedSongs.objects.create(song = songObj, user = userDetailsObj)
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

def getPurchaseLinks(request):
	songId = request.GET.get("songId")
	songObj = song.objects.filter(id = int(songId))
	if (len(songObj) > 0):
		songObj = songObj[0]
		purchaseLinkArr = purchaseSongs.objects.filter(song = songObj)
		purchaseLinkArr = serializers.serialize('json', purchaseLinkArr)
		return HttpResponse(
			json.dumps(
				{
					"status": 1,
					"purchaseLinkArr": purchaseLinkArr
				}), content_type="application/json")
	
