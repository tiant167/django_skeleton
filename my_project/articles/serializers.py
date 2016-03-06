#-*-coding:utf-8-*-
from __future__ import unicode_literals

from base.serializers import BaseSerializer
from .models import Articles

class ArticleSerializer(BaseSerializer):

    class Meta:
        model = Articles
