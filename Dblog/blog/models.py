from django.db import models

# Create your models here.
from django.db import models
# from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


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

    # 第二种完成 updateAt方式
    # def save(self, *args, **kwargs):
    #     self.updatedAt = timezone.now()
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '博客'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
