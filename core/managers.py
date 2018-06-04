from django.db import models

# ... Author and Publisher models here ...

class BookManager(models.Manager):

    def get_books(self):
        
        return self.all()
