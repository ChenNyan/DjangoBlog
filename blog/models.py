from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=64)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = '标签名称'
        verbose_name_plural = '标签列表'
        db_table = 'tag'


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    article_id = models.AutoField(verbose_name='标号', primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', blank=True, null=True)
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    tags_id = models.ForeignKey(Tag, verbose_name='标签ID', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def next_article(self):
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False).first()

    def prev_article(self):
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).first()

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        db_table = 'article'
        get_latest_by = 'created_time'