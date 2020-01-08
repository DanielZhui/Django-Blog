from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    url = models.URLField(blank=True)
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        # 获取的数据默认按时间倒叙
        ordering = ['-createdAt']

    def __str__(self):
        return '{0}: {1}'.format(self.name, self.text[:20])
