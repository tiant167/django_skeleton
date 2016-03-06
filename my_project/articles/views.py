#-*-coding:utf-8-*-
from base.views import BaseView
from .serializers import ArticleSerializer
from .models import Articles
# Create your views here.


class ArticleDetail(BaseView):
    def get(self, request, id):
        article = self.get_object(Articles, id)
        return self.success_response(ArticleSerializer(article).data)


class ArticleList(BaseView):
    def get(self, request, article_type):
        '''
        /api/article/list/{type}/?start=0&num=20
        type: all, CYHW, CYKT (大小写无所谓)
        '''
        query = request.query_params
        start = query.get('start', 0)
        num = query.get('num', 20)
        if start < 0:
            start = 0
        if num < 0:
            num = 20
        article_type = article_type.upper()
        if article_type not in ('CYHW', 'CYKT'):
            article_type = None
        # None == all
        q = Articles.objects.all()
        if article_type:
            q = q.filter(article_type=article_type)
        articles = q.order_by('-created_time')[start:start + num]
        return self.success_response(ArticleSerializer(articles, many=True).data)
