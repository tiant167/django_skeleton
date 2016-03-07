#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

from base.models import BaseModel
# Create your models here.


class Articles(BaseModel):
    TYPE_CHOICE = (
        ('CYHW', u'创业好文'),
        ('CYKT', u'创业课堂')
    )
    title = models.CharField(max_length=200, verbose_name=u'标题')
    description = models.TextField(verbose_name=u'简述')
    url = models.URLField(verbose_name=u'文章链接')
    article_type = models.CharField(max_length=200, choices=TYPE_CHOICE, verbose_name=u'文章类型')
    picture = models.ImageField(upload_to='static/article/%Y/%m/%d', verbose_name=u'图片')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
