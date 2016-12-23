from django.db import models
from authentication.models import userDetails
# Create your models here.

class song(models.Model):
	songName = models.CharField(max_length = 255)
	artist = models.ForeignKey(userDetails)
	coverPic = models.ImageField(upload_to = 'song_covers/')
	dateOfUpload = models.DateTimeField(auto_now_add = True)