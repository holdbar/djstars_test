from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from core.managers import BookManager, RequestLogManager


class Book(models.Model):
    """
    Book model.
    """

    title = models.CharField(verbose_name=_("title"), max_length=256, db_index=True)
    author = models.CharField(verbose_name=_("author"), max_length=256, db_index=True)
    ISBN = models.CharField(verbose_name="ISBN", max_length=20, unique=True, db_index=True)
    price = models.DecimalField(verbose_name=_("price"), max_digits=10, decimal_places=2)
    publish_date = models.DateField(verbose_name=_("publish date"), default=now, db_index=True)

    objects = BookManager()

    class Meta:

        app_label="core"
        verbose_name = _("book")
        verbose_name_plural = _("books")
        unique_together = ["title", "author",]

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
    	
class RequestLog(models.Model):
    """
    HTTP request log model.
    """

    request = models.CharField(verbose_name=_("request"), max_length=2048, editable=False)
    parameters = models.CharField(verbose_name=_("parametres"), max_length=2048, editable=False)
    meta = models.CharField(verbose_name=_("meta"), max_length=2048, editable=False)
    cookies = models.CharField(verbose_name=_("cookies"), max_length=2048, editable=False)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)

    objects = RequestLogManager()

    class Meta:

        app_label="core"
        verbose_name = _("request log")
        verbose_name_plural = _("request logs")
        ordering = ["-created"]

    def __str__(self):

        return self.request


