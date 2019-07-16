from django.contrib import admin
from .models import Book
# Register your models here.
#we have to register individual model or app which we want to display in admin panel

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')      #which fields to show in Books app


admin.site.register(Book, BookAdmin)
#so we have registered model, now it will get display in admin page