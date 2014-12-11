# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='aaa', verbose_name='書籍名', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.IntegerField(blank=True, verbose_name='ページ数', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default=True, verbose_name='出版社', max_length=255),
            preserve_default=True,
        ),
    ]
