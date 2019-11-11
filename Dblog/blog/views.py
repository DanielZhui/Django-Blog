import markdown
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
        'markdown.extensions.toc'
    ])
    article.content = md.convert(article.content)
    article.toc = md.toc
    return render(request, 'blog/detail.html', context={'article': article})