# -*- coding:utf-8 -*-
from django import template
from ..forms import CommentsForm


register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, article, form=None):
    if form is None:
        form = CommentsForm()
    return {
        'form': form,
        'article': article
    }


@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, article):
    comment_list = article.comments_set.all().order_by('-createdAt')
    # comment_list = article.objects.filter(article=article)
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list
    }
