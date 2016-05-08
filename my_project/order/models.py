#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from base.models import BaseModel
# Create your models here.


class Order(BaseModel):
    BAR = 'BAR'
    KTV = 'KTV'
    THREE = 'three'
    SIX_PLUS = 'six+'
    SIX = 'six'
    TWELVE_PLUS = 'twelve+'
    SOURCE_CHOICE = ((BAR, '酒吧街'), (KTV, 'KTV'))
    AMOUNT_CHOICE = (
        (THREE, '3 瓶 - 酒吧街'),
        (SIX_PLUS, '6 瓶以上 - 酒吧街'),
        (SIX, '6 瓶 - KTV'),
        (TWELVE_PLUS, '12 瓶以上 - KTV')
    )
    username = models.CharField(max_length=200, verbose_name=u'姓名')
    phone = models.CharField(max_length=200, verbose_name=u'手机号')
    source = models.CharField(max_length=20, choices=SOURCE_CHOICE, verbose_name=u'购买渠道')
    amount = models.CharField(max_length=20, choices=AMOUNT_CHOICE, verbose_name=u'购买瓶数')
    recipe_num = models.CharField(max_length=200, verbose_name=u'小票单号')

    class Meta:
        unique_together = ('source', 'recipe_num')
        verbose_name = u'订单'
        verbose_name_plural = u'订单'
