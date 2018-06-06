# Generated by Django 2.0.6 on 2018-06-06 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(editable=False, max_length=2048, verbose_name='request')),
                ('parameters', models.CharField(editable=False, max_length=2048, verbose_name='parametres')),
                ('meta', models.CharField(editable=False, max_length=2048, verbose_name='meta')),
                ('cookies', models.CharField(editable=False, max_length=2048, verbose_name='cookies')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created date/time')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'request logs',
                'verbose_name': 'request log',
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(db_index=True, max_length=20, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(db_index=True, max_length=256, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='publish date'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author')},
        ),
    ]
