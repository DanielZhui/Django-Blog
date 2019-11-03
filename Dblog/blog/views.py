from django.shortcuts import render
from django.http import HttpResponse
from . models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all().order_by('created_time')
    return render(request, 'blog/index.html', context={
        'article': articles
    })
