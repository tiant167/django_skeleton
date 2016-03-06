from django.shortcuts import render

from base.views import BaseView
from .serializers import ActivitySerializer
from .models import Activity

# Create your views here.

class ActivityDetail(BaseView):
    def get(self, request, id):
        activity = self.get_object(Activity, id)
        return self.success_response(ActivitySerializer(activity).data)


class ActivityList(BaseView):
    def get(self, request):
        query = request.query_params
        start = query.get('start', 0)
        num = query.get('num', 20)
        if start < 0:
            start = 0
        if num < 0:
            num = 20
        q = Activity.objects.all().order_by('-created_time')[start:start + num]
        return self.success_response(ActivitySerializer(q, many=True).data)
