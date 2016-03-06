#-*-coding:utf-8-*-
from __future__ import unicode_literals

from base.serializers import BaseSerializer
from .models import Activity, ActivityFlow


class ActivityFlowSerializer(BaseSerializer):

    class Meta:
        model = ActivityFlow


class ActivitySerializer(BaseSerializer):
    activityflow_set = ActivityFlowSerializer(value=('start_time', 'end_time', 'description'), many=True)

    class Meta:
        model = Activity
