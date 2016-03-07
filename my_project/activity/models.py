#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

from base.models import BaseModel
# Create your models here.


class Activity(BaseModel):
    title = models.CharField(max_length=200, verbose_name=u'标题')
    description = models.TextField(verbose_name=u'活动详情')
    picture = models.ImageField(upload_to='static/activity/%Y/%m/%d', verbose_name=u'活动图片')
    url = models.URLField(verbose_name=u'活动链接')
    main_organizer = models.CharField(max_length=200, verbose_name=u'主办单位')
    union_organizer = models.CharField(max_length=200, verbose_name=u'联合主办')
    partner = models.CharField(max_length=200, verbose_name=u'合作伙伴')
    activity_time = models.DateTimeField(verbose_name=u'活动时间')
    location = models.CharField(max_length=200, verbose_name=u'活动地点')

    class Meta:
        verbose_name = u'活动'
        verbose_name_plural = u'活动'


class ActivityFlow(BaseModel):
    activity = models.ForeignKey(Activity)
    start_time = models.TimeField(verbose_name=u'开始时间')
    end_time = models.TimeField(verbose_name=u'结束时间')
    description = models.CharField(max_length=200, verbose_name=u'流程说明')

    class Meta:
        verbose_name = u'流程'
        verbose_name_plural = u'流程'
