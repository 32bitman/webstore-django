# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160205_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, verbose_name='Апублікавана', default=datetime.datetime(2016, 2, 5, 17, 46, 41, 353228, tzinfo=utc)),
        ),
    ]
