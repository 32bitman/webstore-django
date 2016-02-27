# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20160209_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 9, 19, 15, 55, 679354, tzinfo=utc), db_index=True, verbose_name='Апублікавана'),
        ),
    ]
