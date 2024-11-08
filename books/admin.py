from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author__name', 'creation_date')
    search_fields = ('title',)
    list_filter = ('author',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
