# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Назва', unique=True)),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Парадкавы нумар', db_index=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name_plural': 'катэгорыі',
                'verbose_name': 'карэгорыя',
            },
        ),
    ]
