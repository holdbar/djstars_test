from django.urls import path, re_path
from core import views

urlpatterns = [
    path('', views.books, name='books'),
    path('edit-books', views.edit_books, name='edit-books'),
]
