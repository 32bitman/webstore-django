# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(unique_for_date='posted', verbose_name='Загаловак', max_length=100)),
                ('description', models.TextField(verbose_name='Скарочаны змест')),
                ('content', models.TextField(verbose_name='Змест')),
                ('posted', models.DateTimeField(db_index=True, verbose_name='Апублікавана', auto_now_add=True)),
                ('is_commentable', models.BooleanField(default=True, verbose_name='Дазвол каментавання')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Тэгі', help_text='A comma-separated list of tags.', blank=True, through='taggit.TaggedItem', to='taggit.Tag')),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'артыкул блогу',
                'verbose_name_plural': 'артыкулы блогу',
                'ordering': ['-posted'],
            },
        ),
    ]
