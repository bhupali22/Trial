from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User     #import default user model
# Create your models here.
#djando itself create database and it interacts or talks with database through models. Model acts as a data layer. Usually single model maps with single database.

#This is our store and we are going to sell books.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):      #whenever django asks who are you then it will return first name and last name. It helps in displaying value of Author field in admin panel
        return "%s, %s" % (self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)         #default value is added while migration as there are existing rows in database so they need to provide default value.
    stock = models.IntegerField(default=0)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()