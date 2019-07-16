from django.urls import path
from . import views  # . means current app or current directory

urlpatterns = [
    path('', views.message),        #here 1st argument already contains localhost:8000/New. In second argument if we put 'views.message' (''), then it gives TypeError

]