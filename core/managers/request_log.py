from django.db import models

class RequestLogManager(models.Manager):
    """
    Request log model manager.
    """

    def get_requests(self):

        return self.all()[:10]
        