from django.conf import settings
from django.db import models

from apps.users.models import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(upload_to='catalog/product/', null=True, blank=True, verbose_name="Фото продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Пользователь')

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return f'{self.name} - {self.price} руб.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('can_change_description', 'Can change description'),
            ('can_change_category', 'Can change category'),
            ('set_published_status', 'Set published status'),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version',
                                verbose_name='Название продукта')
    number_version = models.IntegerField(verbose_name='Номер версии')
    title_version = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='Признак текущей версии', default=True)

    def __str__(self):
        return f'{self.title_version} ({self.product})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
