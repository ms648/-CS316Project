from django.db import models

# Create your models here.


#this is where we write logic that corresponds with database -- business logic

class Member(models.Model):
	name =  models.CharField(max_length = 256)
	email = models.CharField(max_length = 64)

	class Meta:
		db_table = "Members"

	def __str__(self):
		return self.name

class Student(models.Model):
	goals = models.CharField(max_length = 1000)
	student_id = models.IntegerField()

	class Meta:
		db_table = "Students"

	def __str__(self):
		return self.student_id
