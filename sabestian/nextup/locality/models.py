from __future__ import unicode_literals

from django.db import models

# Create your models here.

class areaCodeMapping(models.Model):
	DIVISION_CHOICES = (
		("NorthWestern", "NorthWestern"),
		("SouthWestern", "SouthWestern"),
		("NorthCentral", "NorthCentral"),
		("SouthCentral", "SouthCentral"),
		("NorthEastern", "NorthEastern"),
		("SouthEastern", "SouthEastern")
	)

	areaCode = models.IntegerField()
	region = models.IntegerField()
	state = models.CharField(max_length = 255)
	division = models.CharField(max_length = 255, choices = DIVISION_CHOICES)

	def __str__(self):
		return str(self.areaCode) + " " + self.state