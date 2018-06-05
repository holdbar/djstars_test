from django.db import models

# ... Author and Publisher models here ...

class BookManager(models.Manager):

    def get_books(self):

        return self.all()

    def get_book(self, pk):

        return self.get(pk=pk)
