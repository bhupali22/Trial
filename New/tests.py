# Create your tests here.
from django.test import TestCase
from .models import Book, Author
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from decimal import *


#create class for each of django app
#create method for each model

class StoreViewsTestCase(TestCase):

    def setUp(self):        #It is always there, still we are not going to use this
        self.user = User.objects.create_user(
            username="james", email="some@email.com", password="password"
        )
        author = Author.objects.create(first_name="Stephen", last_name="King")
        book = Book.objects.create(title="Cujo", author=author, description="Darn scary!", price=9.99, stock=1)


    def test_index(self):
        resp = self.client.get('/New/')         #It will hit the url /New/ and will get the response. Its going to use a fake web browser. if you forgot last / then it gives error or test gets failed
        self.assertEqual(resp.status_code, 200)     #The HTTP 200 OK success status response code indicates that the request has succeeded. i.e It got the page
        self.assertTrue('books' in resp.context)       #It will assert True if the context variable in resp contains books
        self.assertTrue(resp.context['books'].count() > 0)      #If we run this test without creating book object in setUp method then this will fail coz right now we dont have any book in test database.

    def test_cart(self):
        resp = self.client.get('/New/cart/')
        self.assertEqual(resp.status_code, 302)     #302 is redirect code. Right Now we are not logged in so we will get redirected as per logic written in view

    def test_book_detail(self):
        resp = self.client.get('/New/book/1/')      #This all test are done for book we created above i.e cujo
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['book'].pk, 1)        #it will check returned pk of book is 1 or not
        self.assertEqual(resp.context['book'].title, "Cujo")
        resp = self.client.get('/New/book/2/')      #this statement itself generate error Book matching query does not exist coz we have not written that logic in views. As we have onle one book whos pk is 2
        self.assertEqual(resp.status_code, 404)     #After writing get_object_or_404 logic in book_details we get success.

    def test_add_to_cart(self):     #for testing this functionality we need to logged in. So in setUp create user
        self.logged_in = self.client.login(username="james", password="password")
        self.assertTrue(self.logged_in)     #checks whether we are logged in
        resp = self.client.get('/New/add/1/')
        resp = self.client.get('/New/cart/')      # trailing / is imp otherwise test will not pass
        self.assertEqual(resp.context['total'], Decimal('9.99'))
        self.assertEqual(resp.context['count'], 1)      #looking count of order
        self.assertEqual(resp.context['cart'].count(), 1)   #looking at count of iteam in cart
        self.assertEqual(resp.context['cart'].get().quantity, 1)