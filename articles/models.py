from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

class Article(models.Model):
    title = models.CharField('Название', max_length=120)
    announce = models.CharField('Анонс', max_length=200)
    text = models.TextField('Статья')
    image = models.ImageField(upload_to='static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, db_index=True, unique=True, default=uuid.uuid4, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        index_together = (('id', 'slug'), )

    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.id, self.slug])

