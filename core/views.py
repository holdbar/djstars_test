from django.shortcuts import render, redirect

from core.models import Book, RequestLog
from core.forms import BookForm

# Create your views here.

def books(request):
    if request.method == "POST":
        if request.POST.get('asc'):
            books = Book.objects.get_books_asc_publish()
        if request.POST.get('desc'):
            books = Book.objects.get_books_desc_publish()                
    else:     
        books = Book.objects.get_books()

    return render(request, 'books.html', {'books': books})

def edit_books(request):
    if request.method == "POST":
        if request.POST.get('pk'):
            book = Book.objects.get_book(request.POST.get('pk'))
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
        else:
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
    books = Book.objects.get_books()
    forms = [(book.pk, BookForm(instance=book)) for book in books]
    form = BookForm()

    return render(request, 'edit_books.html', {'forms': forms, 'form': form})

def requests_log(request):
    requests = RequestLog.objects.get_requests()

    return render(request, 'requests_log.html', {'requests': requests})