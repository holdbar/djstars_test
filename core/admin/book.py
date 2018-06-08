from django.contrib.admin import ModelAdmin

from core.models.book import Book

class BookAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        Book.objects.set_old_instance(obj)
        obj.save()
        