"""Practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from New import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$', views.index, name="index"),         #r stands for regex(regular expression) ^ means starts with and $ means end with and ^$ means nothing
    path('', views.index),
    #path('message/', views.message),
    path('New/', include('New.urls')),      #'' are important in include function otherwise it gives AttributeError. This statement means anything starting with New/ must go to New.urls file to find mapping url
]
