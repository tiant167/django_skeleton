#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from django.db import IntegrityError
from base.views import BaseView
from .models import Order
# Create your views here.

class OrderSubmit(BaseView):
    def post(self, request):
        try:
            data = request.data
            payload = {
                'username' : data['username'],
                'phone' : data['phone'],
                'source' : data['source'],
                'amount' :data['amount'],
                'recipe_num' : data['recipe_num'],
            }
        except (KeyError, TypeError):
            # return self.fail_response(400, 'argument missing')
            raise
        if payload['source'] == Order.BAR:
            if payload['amount'] not in (Order.THREE, Order.SIX_PLUS):
                return self.fail_response(400, 'source amount not compact')
        elif payload['source'] == Order.KTV:
            if payload['amount'] not in (Order.SIX, Order.TWELVE_PLUS):
                return self.fail_response(400, 'source amount not compact')
        else:
            return self.fail_response(400, 'source error')
        try:
            order = Order.objects.create(**payload)
        except IntegrityError:
            return self.fail_response(400, 'recipe exist')
        return self.success_response('ok')
