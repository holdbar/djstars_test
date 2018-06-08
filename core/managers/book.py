from django.db import models

class BookManager(models.Manager):
    '''
    Book model manager.
    '''

    def set_old_instance(self, book):
        book._old_title = book.title
        book._old_author = book.author
        book._old_ISBN = book.ISBN
        book._old_price = book.price
        book._old_publish_date = book.publish_date

    def get_books(self):

        return self.all()

    def get_book(self, pk):

        return self.get(pk=pk)

    def get_books_asc_publish(self):

        return self.all().order_by('publish_date')

    def get_books_desc_publish(self):

        return self.all().order_by('-publish_date')
        