from django import forms
from django.forms.widgets import DateInput

from core.models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        
        fields = ('title', 'author', 'ISBN', 'price','publish_date',)
        widgets = {
            'publish_date': DateInput(attrs={'type': 'date'}),
        }

