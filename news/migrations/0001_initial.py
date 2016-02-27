# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(default=datetime.datetime(2016, 2, 1, 18, 52, 4, 887244), db_index=True, verbose_name='Опубликована')),
            ],
            options={
                'verbose_name_plural': 'новости',
                'ordering': ['-posted'],
                'verbose_name': 'новость',
            },
        ),
    ]
