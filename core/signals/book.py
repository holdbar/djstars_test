from core.models.book_log import BookLog

def pre_delete_book(sender, instance, **kwargs):
    '''
    Add book changes in log on book deletion.

    :param sender: sender model class.
    :type sender: object.
    :param instance: book model instance.
    :type instance: core.models.book.Book.
    :param kwargs: additional args.
    :type kwargs: dict.
    '''

    old_values = {
            'title': instance.title,
            'author': instance.author,
            'ISBN': instance.ISBN,
            'price': instance.price,
            'publish_date': instance.publish_date
        }
    BookLog.objects.create(title=instance.title,
                               author=instance.author, 
                               action='deleted',
                               old_values=old_values)

def post_save_book(sender, instance, created, **kwargs):
    '''
    Add book changes in log on book creation/edition.

    :param sender: sender model class.
    :type sender: object.
    :param instance: book model instance.
    :type instance: core.models.book.Book.
    :param created: is model instance created/edited.
    :type created: bool
    :param kwargs: additional args.
    :type kwargs: dict.
    '''

    if created:        
        BookLog.objects.create(title=instance.title, author=instance.author, action='created')
    else:
        old_values = {
            'title': instance._old_title,
            'author': instance._old_author,
            'ISBN': instance._old_ISBN,
            'price': instance._old_price,
            'publish_date': instance._old_publish_date
        }
        new_values = {
            'title': instance.title,
            'author': instance.author,
            'ISBN': instance.ISBN,
            'price': instance.price,
            'publish_date': instance.publish_date
        }
        BookLog.objects.create(title=instance.title,
                               author=instance.author, 
                               action='updated',
                               old_values=old_values,
                               new_values=new_values)

