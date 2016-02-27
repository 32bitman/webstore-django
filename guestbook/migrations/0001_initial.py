# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user', models.CharField(verbose_name='Пользователь', max_length=20)),
                ('posted', models.DateTimeField(verbose_name='Опубликовано', db_index=True, auto_now_add=True)),
                ('content', models.TextField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'запись гостевой книги',
                'verbose_name_plural': 'записи гостевой книги',
                'ordering': ['-posted'],
            },
        ),
    ]
