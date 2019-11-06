from django.db import models

# Create your models here.


#this is where we write logic that corresponds with database -- business logic

class Member(models.Model):
	name =  models.CharField(max_length = 256)
	email = models.CharField(max_length = 64)

	def __str__(self):
		return self.name
