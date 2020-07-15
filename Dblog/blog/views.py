import re
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from . models import Article, Category, Tag

# Create your views here.


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 访问文章访问量 +1
    article.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    article.content = md.convert(article.content)
    article.toc = md.toc
    # 当文章中不存在目录时,显示空''
    result = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    article.toc = result.group(1) if result is not None else ''
    return render(request, 'blog/detail.html', context={'article': article})


class ArchiveView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return super(ArchiveView, self).get_queryset().filter(createdAt__year=self.kwargs.get('year'), createdAt__month=self.kwargs.get('month')).order_by('createdAt')


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# 标签页面
class TagView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tags).order_by('createdAt')
