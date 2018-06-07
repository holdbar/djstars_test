from django.shortcuts import render

from core.models.book_log import BookLog

def book_log(request):
    book_logs = BookLog.objects.get_book_logs()

    return render(request, 'book_log.html', {'book_logs': book_logs})
