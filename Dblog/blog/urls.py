# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('articles', views.IndexView.as_view(), name='index'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('articles/archives/<int:year>/<int:month>', views.ArchiveView.as_view(), name='archive'),
    path('articles/categories/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('articles/tags/<int:pk>', views.TagView.as_view(), name='tag'),
    path('articles/search', views.search, name='search')
]