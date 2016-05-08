#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from ..base.serializers import BaseSerializer
from .models import Order


class OrderSerializer(BaseSerializer):

    class Meta:
        model = Order
