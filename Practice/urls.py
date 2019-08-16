"""Practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('',      views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('',   Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from New import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),        #by default present for admin site. you’ll be able to use the admin site by visiting the URL you hooked it into (/admin/, by default).
    #url(r'^$', views.inde  x, name="index"),         #r   stands for regex(regular expression) ^ means starts with and $ means end with and ^$ means nothing
    path('', views.index, name='index'),
    #path('accounts/', include('registration.backends.default.urls')),
    path('message/', views.message),
    path('New/', include('New.urls')),      #'' are important in include function otherwise it gives AttributeError. This statement means anything starting with New/ must go to New.urls file to find mapping url
    url(r'^accounts/', include('registration.backends.default.urls')),      #include() function allows referencing other URLConf. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
    # url(r'^store/', include('store.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       #This is going to give us url for media file which django will consider
