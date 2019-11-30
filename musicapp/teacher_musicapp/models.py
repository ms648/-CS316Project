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
	student_id = models.IntegerField(primary_key = True)

	class Meta:
		db_table = "Students"

	def __str__(self):
		return self.student_id

class Teacher(models.Model):
	bio = models.CharField(max_length = 1000)
	teacher_id = models.IntegerField(primary_key = True)

	class Meta:
		db_table = "Teachers"

	def __str__(self):
		return self.teacher_id

class Trackable(models.Model):
	name = models.CharField(max_length = 48)
	instrument = models.CharField(max_length = 48)

	class Meta:
		db_table = "Trackables"

	def __str__(self):
		return self.name + " " + self.instrument

class Recording(models.Model):
	day = models.DateField()
	trackable_name = models.CharField(max_length = 48)
	duration = models.IntegerField()
	location = models.CharField(max_length = 100)
	student = models.IntegerField()

	class Meta:
		db_table = "Recordings"

	def __str__(self):
		return self.trackable_name + " " + str(self.student)

class Note(models.Model):
	student_id = models.IntegerField()
	trackable_name = models.CharField(max_length = 48)
	trackable_instrument = models.CharField(max_length = 48)
	note = models.CharField(max_length = 1000)

	class Meta:
		db_table = "Notes"

	def __str__(self):
		return self.trackable_name + " " + str(self.student_id)

class IsStudentOf(models.Model):
	student_id = models.IntegerField()
	teacher_id = models.IntegerField()
	instrument = models.CharField(max_length = 48)
	start_date = models.DateField()
	end_date = models.DateField()

	class Meta:
		db_table = "IsStudentOf"

	def __str__(self):
		return str(self.teacher_id) + " " + str(self.student_id)

class Creates(models.Model):
	trackable_name = models.CharField(max_length = 48)
	trackable_instrument = models.CharField(max_length = 48)
	teacher_id = models.IntegerField()
	student_id = models.IntegerField()
	date_assigned = models.DateField()
	date_removed = models.DateField()
	active = models.IntegerField()
	current_duration = models.IntegerField()

	class Meta:
		db_table = "Creates"

	def __str__(self):
		return self.trackable_name + " " + str(self.teacher_id)

class IsAssigned(models.Model):
	practice_day = models.DateField()
	time = models.IntegerField()
	student_id = models.IntegerField()
	trackable_name = models.CharField(max_length = 48)
	trackable_instrument = models.CharField(max_length = 48)

	class Meta:
		db_table = "IsAssigned"

	def __str__(self):
		return self.trackable_name