from django.contrib.syndication.views import Feed

from . models import Article

class AllArticlesRssFeed(Feed):
    # 显示聚合阅读器上的标题
    title = 'wollens-blog'

    # 通过聚合阅读器跳转到网站地址
    link = '/'

    # 显示在聚合阅读器上的描叙信息
    description = 'wollens-blog all Articles'

    # 需要显示的内容条目
    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return '{0}-{1}'.format(item.category, item.title)

    # 聚合器中显示内容条目描叙
    def item_description(self, item):
        return item.body_html
