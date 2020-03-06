from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    list_filter = ('last_name', 'first_name')
#admin.site.register(Author, AuthorAdmin)

