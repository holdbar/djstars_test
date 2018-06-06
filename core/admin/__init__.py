from django.contrib import admin

from core.models.book import Book
from core.models.request_log import RequestLog
from core.models.book_log import BookLog

admin.site.register(RequestLog)
admin.site.register(Book)
admin.site.register(BookLog)

