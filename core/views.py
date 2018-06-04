from django.shortcuts import render
from django.http import HttpResponse
from core.models import Book

# Create your views here.

def home(request):
    book = Book()
    response = book.objects.get_books()

    return HttpResponse(response)
