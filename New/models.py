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

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)      #True represents that the cart is still active and it is not processed
    order_date = models.DateField(null=True)        #by default django does not allow fields to be null, if you want null field then you need to set null=TRUE
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def add_to_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(
                book=book,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_from_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except BookOrder.DoesNotExist:
            pass



class BookOrder(models.Model):      #this is for tracking books and its quantity in each cart
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()