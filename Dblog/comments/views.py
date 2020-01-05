from blog.models import Article
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentsForm


@require_POST
def comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentsForm(request.POST)
    if form.is_valid():
        comments = form.save(commit=False)
        comments.article = article
        print('>>>', comments)
        comments.save()
        messages.add_message(request, messages.SUCCESS, '评论发表成功！', extra_tags='success')
        return redirect(article)
    context = {
        'article': article,
        'form': form
    }
    messages.add_message(request, messages.ERROR, '评论格式不对,评论失败', extra_tags='error')
    return render(request, 'comment/preview.html', context=context)
