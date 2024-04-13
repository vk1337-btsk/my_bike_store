from django.db import models
from pytils.translit import slugify


class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    slug = models.CharField(max_length=150, null=True, blank=True, verbose_name='slug')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='catalog/articles/', null=True, blank=True, verbose_name="Превью статьи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    flag_publication = models.BooleanField(verbose_name='Статус публикации')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'Статья: {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
