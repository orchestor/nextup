from django.shortcuts import render
from authentication.models import userDetails 
from music.models import *
from django.http import HttpResponse,Http404
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
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

def uploadSong(request):
	return render(request, "upload.html")

@csrf_exempt
def uploadSongFile(request):
	f = request.FILES["file"]
	print(f.name)
	userDetailsObj = userDetails.objects.filter(user = request.user)
	if (len(userDetailsObj) > 0):
		userDetailsObj = userDetailsObj[0]
		songObj = song.objects.create(songFile = f, artist = userDetailsObj, status = "Incomplete")
	return HttpResponse(
		json.dumps(
			{
				"status": 1,
				"songId": songObj.pk
			}), content_type="application/json")

def uploadSongStep2(request):
	songId = request.GET.get("songId")
	return render(request, "upload-song-step-2.html", {"songId": songId})

def uploadSongDetails(request):
	songId = request.POST.get("songId")
	songName = request.POST.get("songName")
	coverPic = request.FILES["coverPic"]
	genre = request.POST.get("genre")
	purchaseLink1PortalName = request.POST.get("purchaseLink1PortalName")
	purchaseLink1 = request.POST.get("purchaseLink1")
	purchaseLink2PortalName = request.POST.get("purchaseLink2PortalName")
	purchaseLink2 = request.POST.get("purchaseLink2")
	songObj = song.objects.filter(pk = int(songId))
	if (len(songObj) > 0):
		songObj = songObj[0]
		songObj.songName = songName
		songObj.coverPic = coverPic
		songObj.genre = genre
		songObj.status = "Complete"
		songObj.save()
		purchaseLinkObj = purchaseSongs.objects.create(song = songObj, purchasePortalName = purchaseLink1PortalName, purchaseLink = purchaseLink1)
		purchaseLinkObj = purchaseSongs.objects.create(song = songObj, purchasePortalName = purchaseLink2PortalName, purchaseLink = purchaseLink2)
	return HttpResponseRedirect("/")