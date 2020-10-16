from django.contrib import admin
from blog.models import Article, Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    text_fields = ('content')
    list_display = ['article_id', 'title', 'created_time']
    search_fields = ['title']
    list_filter = ['created_time']

admin.site.register(Article, PostAdmin)
admin.site.register(Tag)