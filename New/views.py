from django.shortcuts import render

# Create your views here.
def index(request): #request is an http request object which is passed to view as first argument. This request contains all the imediate information which django needs in order to provide response to browser.
    return render(request, 'template1.html')