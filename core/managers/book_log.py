from django.db import models

class BookLogManager(models.Manager):
    """
    Book log model manager.
    """

    def get_book_logs(self):

        return self.all()
