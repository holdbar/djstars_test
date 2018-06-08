from django.shortcuts import render

from core.models.book import Book
from core.forms.book import BookForm

def edit_books(request):
    if request.method == 'POST':
        if request.POST.get('pk'):
            book = Book.objects.get_book(request.POST.get('pk'))
            Book.objects.set_old_instance(book)
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
