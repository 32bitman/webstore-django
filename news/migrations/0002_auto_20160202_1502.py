# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(verbose_name='Опубликована', db_index=True, default=datetime.datetime(2016, 2, 2, 15, 2, 14, 283289)),
        ),
    ]
