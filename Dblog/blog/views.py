from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all().order_by('createdAt')
    print('>>>', articles)
    return render(request, 'blog/index.html', context={
        'articles': articles
    })


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', context={'article': article})