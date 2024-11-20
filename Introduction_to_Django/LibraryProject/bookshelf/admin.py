from django.contrib import admin

# Register your models here.
from .models import Book

# Define a custom ModelAdmin for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ['title', 'author', 'publication_year']

    # Add search functionality
    search_fields = ['title', 'author']

    # Add filtering capability by author
    list_filter = ['author',]

# Register the Book model with the Django admin interface
admin.site.register(Book, BookAdmin)
# Register your models here.
