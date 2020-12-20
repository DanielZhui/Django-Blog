# -*- coding:utf-8 -*-
from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('articles/comment/<int:article_pk>', views.comment, name='comment')
]