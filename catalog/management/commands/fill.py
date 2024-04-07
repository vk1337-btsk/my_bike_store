import json
import os
from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "This method populates the application's database catalog"

    @staticmethod
    def read_fixtures_json(filename: str) -> list:
        """Retrieving data from a fixture file in the format"""
        with open(rf'{BASE_DIR}\catalog\fixtures\{filename}.json', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):
        """This method populates the application's database catalog"""

        Product.objects.all().delete()
        Category.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE catalog_category, catalog_product RESTART IDENTITY CASCADE;")

        data_category = Command.read_fixtures_json('catalog_category_data')
        data_product = Command.read_fixtures_json('catalog_product_data')

        category_for_create = []
        product_for_create = []

        for category in data_category:
            category_for_create.append(Category(pk=category['pk'],
                                                name=category['fields']['name'],
                                                description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in data_product:
            product_for_create.append(Product(pk=product['pk'],
                                              name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))

        Product.objects.bulk_create(product_for_create)
