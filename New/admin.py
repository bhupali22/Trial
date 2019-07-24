from django.contrib import admin
from .models import Book, Author
# Register your models here.
#we have to register individual model or app which we want to display in admin panel

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')      #which fields to show in Books app. Now we have defined author as foreign key so it will not display any fields in admin panel if we want to display author field. So we removed author field. After setting author field again manually we can add author entry here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
#so we have registered model, now it will get display in admin page