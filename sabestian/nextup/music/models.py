from django.db import models
from authentication.models import userDetails
# Create your models here.

class song(models.Model):
	GENRES = (
		('Alternative', 'Alternative'),
		('Country', 'Country'),
		('EDM', 'EDM'),
		('Metal', 'Metal'),
		('Indie', 'Indie'),
		('Latin Pop', 'Latin Pop'),
		('R&B', 'R&B'),
		('Hip-Hop', 'Hip-Hop'),
		('Rock/Oldies', 'Rock/Oldies'),
		('Dancehall', 'Dancehall')
	)

	songName = models.CharField(max_length = 255)
	artist = models.ForeignKey(userDetails)
	coverPic = models.ImageField(upload_to = 'song_covers/')
	dateOfUpload = models.DateTimeField(auto_now_add = True)
	songFile = models.FileField(upload_to = 'song_file/')
	numberOfLikes = models.BigIntegerField(default = 0)
	genre = models.CharField(max_length = 255, choices = GENRES)

	def __str__(self):
		return self.songName + " " + self.artist.userHandle

class likedSongs(models.Model):
	song = models.ForeignKey(song)
	user = models.ForeignKey(userDetails)
	dateTime = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.song.songName + " " + self.user.userHandle