from django.urls import path
from .views import search_book, book_list, save_selected_books

app_name = 'book'

urlpatterns = [
    path('search/',  search_book, name='search_book'),
    path('list/', book_list, name='book_list'),
    path('save/', save_selected_books, name='save_selected_books'),
    # path('template/', search_book, name='template') # html template
]