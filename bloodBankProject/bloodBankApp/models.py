from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	doner = models.ForeignKey(User, on_delete=models.CASCADE)
	as_choice = [
		("O Positive" , "O Positive"),
		("O Negative" , "O Negative"),
		("A Positive" , "A Positive"),
		("A Negative" , "A Negative"),
		("B Positive" , "B Positive"),
		("B Negative" , "B Negative"),
		("AB Positive" , "AB Positive"),
		("AB Negative" , "AB Negative"),
	]
	bloodgroup = models.CharField(max_length=20, blank=True, null=True, choices=as_choice) 
	email = models.EmailField(null=True, max_length=255)
	phone = models.CharField(null=True, max_length=255)
	situation = models.TextField(default="Please Be a helping hand!")
	postDate = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + " | " + str(self.doner)


	def get_absolute_url(self):
		return reverse("home")
