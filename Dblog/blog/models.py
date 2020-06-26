from django.db import models

import markdown
from django.db import models
# from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import strip_tags


class Category(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = '博客分类'

    def __str__(self):
        return '%s' % self.name


class Tag(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = '博客标签'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 文章摘要允许为空
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, editable=True)

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite'
        ])
        self.excerpt = strip_tags(md.convert(self.content))[:60]
        super().save(*args, **kwargs)

    # 第二种完成 updateAt方式
    # def save(self, *args, **kwargs):
    #     self.updatedAt = timezone.now()
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '博客'
        # 获取的数据默认按时间倒叙
        ordering = ['-createdAt']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
