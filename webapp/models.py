from django.db import models

class movie(models.Model):
	name = models.CharField(max_length=250)
	cast = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	year = models.IntegerField()

	def __str__(self):
		return self.name
