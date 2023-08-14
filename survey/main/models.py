from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=264)
    email=models.CharField(max_length=264)
    batch=models.CharField(max_length=264)