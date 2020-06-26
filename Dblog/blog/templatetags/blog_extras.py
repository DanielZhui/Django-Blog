# -*- coding:utf-8 -*-

from django import template
from django.db.models.aggregates import Count

from ..models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_post.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Article.objects.all().order_by('-createdAt')[:num]
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        # 按月查询
        'date_list': Article.objects.dates('createdAt', 'month', order='DESC')
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(article_count=Count('article')).filter(article_count__gte=0)
    return {
        'category_list': category_list
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all()
    }
