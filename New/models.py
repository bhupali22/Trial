from django.db import models
from django.utils import timezone
# Create your models here.
#djando itself create database and it interacts or talks with database through models. Model acts as a data layer. Usually single model maps with single database.

#This is our store and we are going to sell books.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)         #default value is added while migration as there are existing rows in database so they need to provide default value.
    stock = models.IntegerField(default=0)