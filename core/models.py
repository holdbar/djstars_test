from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.db.models.signals import post_save

from core.managers import BookManager, RequestLogManager, BookLogManager
from core.signals import post_save_book


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

        app_label = "core"
        verbose_name = _("request log")
        verbose_name_plural = _("request logs")
        ordering = ["-created"]

    def __str__(self):

        return self.request


class BookLog(models.Model):
    """
    Book edit log.
    """

    title = models.CharField(verbose_name=_("title"), max_length=256, db_index=True, editable=False)
    author = models.CharField(verbose_name=_("author"), max_length=256, db_index=True, editable=False)
    action = models.CharField(verbose_name=_("action"), max_length=16, db_index=True, editable=False)
    change_field = models.CharField(verbose_name=_("change field"), max_length=16, blank=True, null=True, db_index=True, editable=False)
    old_value = models.CharField(verbose_name=_("old value"), max_length=256, blank=True, null=True, editable=False)
    new_value = models.CharField(verbose_name=_("new value"), max_length=256, blank=True, null=True, editable=False)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)

    objects = BookLogManager()

    class Meta:

        app_label = "core"
        verbose_name = _("book log")
        verbose_name_plural = _("book logs")
        ordering = ["created"]

    
post_save.connect(post_save_book, sender=Book)
