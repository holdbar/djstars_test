from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.db.models.signals import post_save

from core.managers.book_log import BookLogManager

class BookLog(models.Model):
    '''
    Book edit log.
    '''

    title = models.CharField(verbose_name=_('title'), max_length=256, db_index=True, editable=False)
    author = models.CharField(verbose_name=_('author'), max_length=256, db_index=True, editable=False)
    action = models.CharField(verbose_name=_('action'), max_length=16, db_index=True, editable=False)
    old_values = models.CharField(verbose_name=_('old values'), max_length=1024, blank=True, null=True, editable=False)
    new_values = models.CharField(verbose_name=_('new values'), max_length=1024, blank=True, null=True, editable=False)
    created = models.DateTimeField(verbose_name=_('created date/time'), blank=True, null=True, db_index=True, auto_now_add=True)

    objects = BookLogManager()

    class Meta:

        app_label = 'core'
        verbose_name = _('book log')
        verbose_name_plural = _('book logs')
        ordering = ['created']
