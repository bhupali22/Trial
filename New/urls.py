from django.urls import path
from django.conf.urls import url
from . import views  # . means current app or current directory

urlpatterns = [
    path('', views.message),        #here 1st argument already contains localhost:8000/New. In second argument if we put 'views.message' (''), then it gives TypeError
    url(r'^book/(\d+)', views.book_details, name='book_details'),   #when the url is store/book/book_id, it will pass book id to view
]