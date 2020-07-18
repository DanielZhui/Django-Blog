# -*- coding:utf-8 -*-

from django import template
from django.db import connection
from django.db.models import Count

from ..models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_post.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Article.objects.all().order_by('-createdAt')[:num]
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    # TODO: 按月统计文章数还未完成
    select = {'month': connection.ops.date_trunc_sql('year', 'createdAt')}
    count = Article.objects.extra(select=select).values('month').annotate(number=Count('id'))
    return {
        # 按月查询
        'date_list': Article.objects.dates('createdAt', 'month', order='DESC')
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    from django.db.models.aggregates import Count
    category_list = Category.objects.annotate(article_count=Count('article')).filter(article_count__gte=0)
    return {
        'category_list': category_list
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_obj_list = []
    tag_list = Tag.objects.all()
    for tag in tag_list:
        tag_obj = {}
        count = Article.objects.filter(tags=tag).count()
        tag_obj['name'] = tag.name
        tag_obj['pk'] = tag.id
        tag_obj['count'] = count
        tag_obj_list.append(tag_obj)
    return {
        'tag_obj_list': tag_obj_list
    }
