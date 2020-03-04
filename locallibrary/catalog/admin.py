from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

#define the main class 
class AuthorAdmin(admin.ModelAdmin)
    list_display = ('last_name', 'first_name', 'date_of_birth', ' date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

#register the admin class with the association model
admin.site.register(Author, AuthorAdmin)

# register the Admin classes for book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
