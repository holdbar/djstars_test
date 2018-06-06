from django.urls import path, re_path
from django.views.i18n import JavaScriptCatalog
from core.views import books, edit_books, requests_log

urlpatterns = [
    path('', books.books, name='books'),
    path('edit-books', edit_books.edit_books, name='edit-books'),
    path('requests-log', requests_log.requests_log, name='requests-log'),
]
