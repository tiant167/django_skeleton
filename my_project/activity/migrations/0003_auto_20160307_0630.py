# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20160307_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityflow',
            name='end_time',
            field=models.TimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='activityflow',
            name='start_time',
            field=models.TimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]