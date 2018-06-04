from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _

from core.managers import BookManager


class Book(models.Model):
    """
    Book model.
    """

    title = models.CharField(verbose_name=_("title"), max_length=256, db_index=True)
    author = models.CharField(verbose_name=_("author"), max_length=256)
    ISBN = models.CharField(verbose_name="ISBN", max_length=20)
    price = models.DecimalField(verbose_name=_("price"), max_digits=10, decimal_places=2)

    objects = BookManager()

    class Meta:

        app_label="core"
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):

        return self.title
        

class User(AbstractUser):
    """
    User model.
    """

    objects = UserManager()

    class Meta:

        app_label = "core"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):

    	return self.username
    	