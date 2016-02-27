# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160202_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 4, 10, 29, 14, 338139, tzinfo=utc), verbose_name='Опубликована', db_index=True),
        ),
    ]
