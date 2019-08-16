from django.urls import path
from django.conf.urls import url, include
from . import views  # . means current app or current directory
import debug_toolbar

urlpatterns = [
    path('', views.message, name='index'),        #here 1st argument already contains localhost:8000/New. In second argument if we put 'views.message' (''), then it gives TypeError
    url(r'^book/(\d+)', views.book_details, name='book_details'),   #when the url is store/book/book_id, it will pass book id to view
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),     #d represents digit. w is used for alphanumeric
    url(r'^cart/', views.cart, name='cart'),
    #path('__debug__/', include(debug_toolbar.urls)),
]