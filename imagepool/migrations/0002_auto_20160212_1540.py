# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagepool', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagepool',
            options={'verbose_name': 'выява', 'verbose_name_plural': 'выявы', 'ordering': ['user', '-uploaded']},
        ),
        migrations.AlterField(
            model_name='imagepool',
            name='image',
            field=models.ImageField(verbose_name='Выява', upload_to='imagepool/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='imagepool',
            name='uploaded',
            field=models.DateTimeField(db_index=True, verbose_name='Выгружаны', auto_now_add=True),
        ),
    ]
