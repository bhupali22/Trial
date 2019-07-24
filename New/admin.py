from django.contrib import admin
from .models import Book
# Register your models here.
#we have to register individual model or app which we want to display in admin panel


# If you are happy with the default admin interface, you don’t need to define a ModelAdmin object at all – you can register the model class without providing a ModelAdmin description. i.e. admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):      #ModelAdmin class is created as we want custom values. Otherwise a default admin interface will be provided.
    list_display = ('title', 'author', 'price', 'stock')      #which fields to show in Books app


admin.site.register(Book, BookAdmin)
#so we have registered model, now it will get display in admin page