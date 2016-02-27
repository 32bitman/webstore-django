# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestbook',
            options={'verbose_name_plural': 'запісы гасцёвай кнігі', 'ordering': ['-posted'], 'verbose_name': 'запіс гасцёвай кнігі'},
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='content',
            field=models.TextField(verbose_name='Змест'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='posted',
            field=models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Апублікавана'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='user',
            field=models.CharField(max_length=20, verbose_name='Карыстач'),
        ),
    ]
