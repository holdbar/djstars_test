from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from core.managers.request_log import RequestLogManager

    	
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
