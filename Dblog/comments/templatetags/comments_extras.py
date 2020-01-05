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
