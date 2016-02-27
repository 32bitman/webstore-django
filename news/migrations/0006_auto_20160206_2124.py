# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160205_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(verbose_name='Апублікавана', default=datetime.datetime(2016, 2, 6, 18, 24, 19, 293235, tzinfo=utc), db_index=True),
        ),
    ]
