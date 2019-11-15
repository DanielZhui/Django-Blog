import re
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import Article

# Create your views here.


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
