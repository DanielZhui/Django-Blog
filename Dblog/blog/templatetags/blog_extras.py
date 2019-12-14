# -*- coding:utf-8 -*-

from django import template

from ..models import Article, Category, Tag

register = template.Library()
