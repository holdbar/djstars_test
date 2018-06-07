from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.db.models.signals import post_save, pre_delete

from core.models.book_log import BookLog
from core.managers.book import BookManager
from core.signals.book import post_save_book, pre_delete_book


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
        
post_save.connect(post_save_book, sender=Book)
pre_delete.connect(pre_delete_book, sender=Book)

