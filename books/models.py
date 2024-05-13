from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
import uuid

class Section(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('bookstore:book_list_by_genre', args=[self.slug])

class Book(models.Model):
        section = models.ForeignKey(Section,
                                    related_name='books',
                                    on_delete=models.CASCADE)
        title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
        slug = models.CharField(max_length=150, db_index=True, unique=True, default=uuid.uuid4, verbose_name='Ссылка')
        author = models.CharField(max_length=150, db_index=True, verbose_name='Автор')
        cover_image = models.ImageField(upload_to='books/img/covers/%Y/%m/%d', blank=True, verbose_name='Обложка')
        description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
        rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Рейтинг', default=0.00)
        published_date = models.DateField(verbose_name='Дата публикации')
        created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
        updated = models.DateTimeField(auto_now=True, verbose_name='Изменен')

        class Meta:
            ordering = ('title',)
            verbose_name = 'Книга'
            verbose_name_plural = 'Книги'
            index_together = (('id', 'slug'),)

        def __str__(self):
            return self.title

    # def get_absolute_url(self):
    #     return reverse('books:book_detail', args=[self.id, self.slug])
