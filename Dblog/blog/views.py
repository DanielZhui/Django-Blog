import re
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin
from django.contrib import messages
from django.db.models import Q

from . models import Article, Category, Tag

# Create your views here.


class IndexView(PaginationMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    # ListView 中已经封装好 pagination，只需要指定 pagination_by 属性后开启分页功能，代表每一页包含多少篇文章
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    # def get_object(self, queryset=None):
    #     article = super().get_object(queryset=None)
    #     md = markdown.Markdown(extensions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #         TocExtension(slugify=slugify),
    #     ])
    #     article.content = md.convert(article.content)
    #     # 当文章中不存在目录时,显示空''
    #     result = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    #     article.toc = result.group(1) if result is not None else ''
    #     return article


class ArchiveView(PaginationMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return super(ArchiveView, self).get_queryset().filter(createdAt__year=self.kwargs.get('year'), createdAt__month=self.kwargs.get('month')).order_by('createdAt')


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# 标签页面
class TagView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tags).order_by('createdAt')

# 文章搜索
def search(request):
    q = request.GET.get('q').strip(' ')
    print('>>', q)

    if not q:
        err_msg = '请输入搜索关键词'
        messages.add_message(request, messages.ERROR, err_msg, extra_tags='denger')
        return redirect('blog:index')

    articles = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'blog/index.html', {'articles': articles})