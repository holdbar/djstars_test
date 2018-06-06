from core.models import BookLog

def post_save_book(sender, instance, created, **kwargs):
    """
    Add book changes in log on book creation.

    :param sender: sender model class.
    :type sender: object.
    :param instance: book model instance.
    :type instance: core.models.Book.
    :param created: is model instance created/edited.
    :type created: bool
    :param kwargs: additional args.
    :type kwargs: dict.
    """

    if created:        
        BookLog.objects.get_or_create(title=instance.title, author=instance.author, action='created')
