from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()

class Image(models.Model):
	image=models.ImageField(upload_to='myimage')
	date=models.DateTimeField(auto_now_add=True)	