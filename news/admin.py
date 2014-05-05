from django.contrib import admin
from news.models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','text_markdown','pub_date','image']
admin.site.register(Article, ArticleAdmin)
