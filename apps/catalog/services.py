from django.conf import settings
from django.core.cache import cache

from apps.catalog.models import Category, Product


def get_categories_from_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    return category_list


def get_products_from_cache():
    if settings.CACHE_ENABLED:
        key = 'product_list'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.all()
            cache.set(key, product_list)
    else:
        product_list = Product.objects.all()

    return product_list
