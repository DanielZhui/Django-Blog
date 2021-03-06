from django.contrib import admin
from . models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'createdAt', 'updatedAt', 'category', 'author']
    list_editable = ['title', 'content', 'author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
