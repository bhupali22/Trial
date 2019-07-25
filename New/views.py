from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Book, BookOrder, Cart

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

def add_to_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user=request.user
                )
                cart.save()
            cart.add_to_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def remove_from_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user.id, active=True)
        orders = BookOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')