from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'article', 'createdAt']
    filter = ['name', 'article']


admin.site.register(Comments, CommentsAdmin)
