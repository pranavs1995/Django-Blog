from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#One to Many Relationship - One user many posts

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #Many posts can have repeated authors, authors are coming from users

	def __str__(self):
		return(self.title)