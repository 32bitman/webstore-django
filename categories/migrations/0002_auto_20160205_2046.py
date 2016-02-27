# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveSmallIntegerField(db_index=True, unique=True, verbose_name='Парадкавы нумар', default=0),
        ),
    ]
