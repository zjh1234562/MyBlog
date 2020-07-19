from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from ckeditor.fields import RichTextField

# 别忘了导入ArticlerPost
from .models import ArticlePost, ArticleColumn


# 注册ArticlePost到admin中
#admin.site.register(ArticlePost)

@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display=('title','author','total_views')

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'




# 注册文章栏目
#admin.site.register(ArticleColumn)

@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
