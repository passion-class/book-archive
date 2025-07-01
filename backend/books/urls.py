from django.urls import path
from .views import search_book, book_list

app_name = 'book'

urlpatterns = [
    path('search/',  search_book, name='search_book'),
    path('list/', book_list, name='book_list'),
    # path('template/', search_book, name='template') # html template
]