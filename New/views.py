from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request): #request is an http request object which is passed to view as first argument. This request contains all the imediate information which django needs in order to provide response to browser.
    return render(request, 'template1.html')


def message(request):
    books = Book.objects.all()          #inbuild model functionality where all() will return all the objects or books in Book Model or database and count() will return count of objects
    context = {
        'books' : books,
        #'page' : 'welcome to mystery book!'
    }       #data is going to go in template through context variable
    #request.session['location'] = "unknown"
    #if request.user.is_authenticated:
    #    request.session['location'] = "Earth"
    return render(request, 'base.html',context)      #throgth context variable we are passing values to template


def book_details(request, book_id):         #book_id will come from url
    context = {
        'book': Book.objects.get(pk=book_id),
    }
    return render(request, 'New/details.html', context)