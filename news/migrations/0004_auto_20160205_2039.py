# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20160204_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'навіна', 'verbose_name_plural': 'навіны', 'ordering': ['-posted']},
        ),
        migrations.AlterField(
            model_name='new',
            name='content',
            field=models.TextField(verbose_name='Поўны змест'),
        ),
        migrations.AlterField(
            model_name='new',
            name='description',
            field=models.TextField(verbose_name='Скарочаны змест'),
        ),
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 5, 17, 39, 3, 379539, tzinfo=utc), db_index=True, verbose_name='Апублікавана'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(verbose_name='Загаловак', max_length=100, unique_for_date='posted'),
        ),
    ]
