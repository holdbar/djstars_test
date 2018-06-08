from django import forms
from django.forms.widgets import DateInput, TextInput, NumberInput

from core.models.book import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        
        fields = ('title', 'author', 'ISBN', 'price','publish_date',)
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}), 
            'author': TextInput(attrs={'class': 'form-control'}), 
            'ISBN': TextInput(attrs={'class': 'form-control'}), 
            'price': NumberInput(attrs={'class': 'form-control'}),
            'publish_date': DateInput(attrs={'type': 'date'}),

        }

