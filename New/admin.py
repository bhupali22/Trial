from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, Author, BookOrder, Cart
# Register your models here.
#we have to register individual model or app which we want to display in admin panel

class BookAdmin(admin.ModelAdmin):              #The ModelAdmin class is the representation of a model in the admin interface.
    list_display = ('title', 'author', 'price', 'stock', 'Book_Image')      #which fields to show in Books app. Now we have defined author as foreign key so it will not display any fields in admin panel if we want to display author field. So we removed author field. After setting author field again manually we can add author entry here.

    def Book_Image(self, obj):
        return mark_safe('<img src="{url}" width="400px" height="400px" />'.format(
            url=obj.cover_image.url,
        )
        )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'cart', 'quantity')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'order_date')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
#so we have registered model, now it will get display in admin page
admin.site.register(BookOrder, BookOrderAdmin)
admin.site.register(Cart, CartAdmin)