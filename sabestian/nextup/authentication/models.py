from django.db import models
from django.contrib.auth.models import User
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
	areaCode = models.IntegerField()

	def __str__(self):
		return self.userHandle