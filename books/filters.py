from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Author, Book


class AuthorFilterClass(AutoRQLFilterClass):
    MODEL = Author


class BookFilterClass(AutoRQLFilterClass):
    MODEL = Book
    FILTERS = [
        {'filter': 'author',  
         'source': 'author__name'
        },
    ]
