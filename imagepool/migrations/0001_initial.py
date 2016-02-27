# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePool',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('uploaded', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Выгружен')),
                ('image', models.ImageField(upload_to='imagepool/%Y/%m', verbose_name='Изображение')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', '-uploaded'],
                'verbose_name_plural': 'изображения',
                'verbose_name': 'изображение',
            },
        ),
    ]
