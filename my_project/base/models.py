#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Plain(models.Model):
    '''
    Plain abstract models class with nothing
    '''
    class Meta:
        abstract = True


class BaseModel(models.Model):
    '''
    Abstract models class with created_time and updated_time
    '''
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
