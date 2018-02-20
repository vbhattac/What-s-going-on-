from django.db import models

#User class for built-in authentication module
from django.contrib.auth.models import User

class Event(models.Model):
	name = models.CharField(max_length=40)
	time = models.DateTimeField()
	organizer = models.ManyToManyField(User, related_name='organizer')
	### a list of user that organise the event
	participent = models.ManyToManyField(User, related_name='participent', blank=True)
	### a list of user that is going to participate the event
	info = models.CharField(max_length=1000)
	### event discription
	photo = models.ImageField(upload_to="images", blank=True)
	### option to upload: a photo about the event
	###location = xxxx
	privacy = models.CharField(max_length=8)
	### private(friends only) or public. 
	###when implement it in views.py, only input 'private' or 'public'
	price = models.IntegerField(null= True, blank=True)

	def get_events():
		return Event.objects.all().order_by('-time')


class Profile(models.Model):
	owner = models.ForeignKey(User)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	friendlist = models.ManyToManyField(User, related_name='friend', blank=True)
	### a list of user that person friends with
	bio = models.CharField(max_length=420, blank=True)
	photo = models.ImageField(upload_to="images", blank=True)
	age = models.IntegerField(null= True, blank=True)
	events = models.ManyToManyField(Event, related_name='events', blank=True)
	##a list of events that the user went to or is going


	def __str__(self):
		return (self.first_name + self.last_name)


	

	
