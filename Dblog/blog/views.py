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


def index(request):
    articles = Article.objects.all().order_by('createdAt')
    for article in articles:
        article.content = markdown.markdown(article.content,
                               extensions=[
                                   'markdown.extensions.extra',
                                   'markdown.extensions.codehilite',
                                   'markdown.extensions.toc'
                               ])
    return render(request, 'blog/index.html', context={
        'articles': articles
    })


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 访问文章访问量 +1
    article.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc'
        TocExtension(slugify=slugify),
    ])
    article.content = md.convert(article.content)
    article.toc = md.toc
    # 当文章中不存在目录时,显示空''
    result = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    article.toc = result.group(1) if result is not None else ''
    return render(request, 'blog/detail.html', context={'article': article})


# 归档函数
def archive(request, year, month):
    articles = Article.objects.filter(
        createdAt__year=year,
        createdAt__month=month,
    ).order_by('createdAt')
    return render(request, 'blog/index.html', context={'articles': articles})


# 分类页面
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(category=cate).order_by('-createdAt')
    return render(request, 'blog/index.html', context={'articles': articles})


# 标签页面
def tag(request, pk):
    tags = get_object_or_404(Tag, pk=pk)
    articles = Article.objects.filter(tags=tags).order_by('createdAt')
    return render(request, 'blog/index.html', context={'articles': articles})