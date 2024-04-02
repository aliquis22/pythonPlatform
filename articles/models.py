from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField('Название', max_length=120)
    announce = models.CharField('Анонс', max_length=200)
    text = models.TextField('Статья')
    image = models.ImageField(upload_to='static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'