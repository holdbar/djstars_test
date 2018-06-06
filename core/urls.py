from django.urls import path, re_path
from django.views.i18n import JavaScriptCatalog
from core import views

urlpatterns = [
    path('', views.books, name='books'),
    path('edit-books', views.edit_books, name='edit-books'),
    path('requests-log', views.requests_log, name='requests-log'),
]
