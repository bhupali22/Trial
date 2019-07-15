from django.db import models
from django.utils import timezone
# Create your models here.
#djando itself create database and it interacts or talks with database through models. Model acts as a data layer. Usually single model maps with single database.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)