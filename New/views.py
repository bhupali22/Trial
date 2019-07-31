from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BookOrder, Cart, Review
from .forms import ReviewForm


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
    book = get_object_or_404(Book, id=book_id)      #this will prevent from error Book matching query does not exist. And will say page does not exist when book_id does not exist in database.
    #book = Book.objects.get(pk=book_id)
    context = {
        'book': book,
    }
    if request.user.is_authenticated:
        if request.method == "POST":        #check whether form is posted or not
            form = ReviewForm(request.POST)     #creating object of ReviewForm
            if form.is_valid():         #built in function which checks all form fields are valid
                new_review = Review.objects.create(         #CREATING OBJECT OF Review table
                    user=request.user,
                    book=context['book'],
                    text=form.cleaned_data.get('text')          #cleaned_data is attribute field of form and it holds all the cleaned data from that form i.e. striping out white space, tags, etc. It assures text is formatted correctly
                )
                new_review.save()
        else:       #if request is get
            #if Review.objects.filter(user=request.user, book=context['book'].count() == 0):        () is misplaced so it gives attributeError Book has no attribute count
            if Review.objects.filter(user=request.user, book=context['book']).count() == 0:         #checking whether reviews exist for this user or not. If not then show the review form
                form = ReviewForm()
                context['form'] = form

    context['reviews'] = book.review_set.all()      #getting review set
    return render(request, 'New/details.html', context)

def add_to_cart(request, book_id):
    if request.user.is_authenticated:
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
    if request.user.is_authenticated:
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
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user.id, active=True)
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
        return render(request, 'New/cart.html', context)
    else:
        return redirect('index')

