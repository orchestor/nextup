from django.db import models
from django.contrib.auth.models import User
from locality.models import areaCodeMapping
# Create your models here.

class userDetails(models.Model):
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female')
	)

	USER_TYPE = (
		('Artist', 'Artist'),
		('Listener', 'Listener')
	)

	user = models.ForeignKey(User)
	userHandle = models.CharField(max_length = 255)
	age = models.IntegerField()
	gender = models.CharField(max_length = 10, choices = GENDER)
	type = models.CharField(max_length = 10, choices = USER_TYPE)
	areaCode = models.ForeignKey(areaCodeMapping)
	profilePicture = models.ImageField(upload_to = "user-profile-picture/")

	def __str__(self):
		return self.userHandle

class follow(models.Model):
	follower = models.ForeignKey(User, related_name="follower")
	following = models.ForeignKey(User, related_name="following")

	def __str__(self):
		return self.follower.firstName + " is following " + self.following.firstName