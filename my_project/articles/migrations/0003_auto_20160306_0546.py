# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160306_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='picture',
            field=models.ImageField(upload_to='%Y/%m/%d', verbose_name='\u56fe\u7247'),
        ),
    ]
