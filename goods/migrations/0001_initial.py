# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20160205_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Назва', db_index=True, unique=True)),
                ('description', models.TextField(verbose_name='Скарочанае апісанне')),
                ('content', models.TextField(verbose_name='Поўнае апісанне')),
                ('price', models.FloatField(verbose_name='Кошт, Br.', db_index=True)),
                ('price_acc', models.FloatField(null=True, verbose_name='Кошт са зніжкай, Br.', blank=True)),
                ('in_stock', models.BooleanField(verbose_name='У наяўнасці', default=True, db_index=True)),
                ('featured', models.BooleanField(verbose_name='Прапануемы', default=False, db_index=True)),
                ('image', models.ImageField(verbose_name='Асноўная выява', upload_to='goods/list')),
                ('category', models.ForeignKey(verbose_name='Катэгорыя', to='categories.Category')),
            ],
            options={
                'verbose_name': 'тавар',
                'verbose_name_plural': 'тавары',
            },
        ),
        migrations.CreateModel(
            name='GoodImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(verbose_name='Дадатковая выява', upload_to='goods/detail')),
                ('good', models.ForeignKey(to='goods.Good')),
            ],
            options={
                'verbose_name': 'выява да тавару',
                'verbose_name_plural': 'выявы да тавару',
            },
        ),
    ]
