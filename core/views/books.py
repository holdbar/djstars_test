from django.shortcuts import render

from core.models.book import Book

def books(request):
    if request.method == 'POST':
        if request.POST.get('asc'):
            books = Book.objects.get_books_asc_publish()
        if request.POST.get('desc'):
            books = Book.objects.get_books_desc_publish()                
    else:     
        books = Book.objects.get_books()

    return render(request, 'books.html', {'books': books})
