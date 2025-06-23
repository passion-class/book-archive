from django.urls import path
from .views import search_book

urlpatterns = [
    path('search/',  search_book, name='search_book'),
]