# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20160209_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 15, 12, 35, 32, 711191, tzinfo=utc), verbose_name='Апублікавана', db_index=True),
        ),
    ]
