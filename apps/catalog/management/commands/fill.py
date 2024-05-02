import json
from django.core.management import BaseCommand
from django.db import connection
from apps.catalog.models import Category, Product, Version
from apps.journal.models import Articles
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "This method populates the application's database catalog"

    @staticmethod
    def read_fixtures_json(dir_name: str, filename: str) -> list:
        """Retrieving data from a fixture file in the format"""
        with open(rf'{BASE_DIR}\fixtures\{dir_name}\{filename}.json', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):
        """This method populates the application's database catalog"""

        Product.objects.all().delete()
        Category.objects.all().delete()
        Version.objects.all().delete()
        Articles.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE catalog_category, catalog_product RESTART IDENTITY CASCADE;")

        data_category = Command.read_fixtures_json('catalog', '001_categories_data')
        category_for_create = []
        for category in data_category:
            category_for_create.append(
                Category(name=category['fields']['name'],
                         description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        data_product = Command.read_fixtures_json('catalog', '002_products_data')
        product_for_create = []
        for product in data_product:
            product_for_create.append(Product(name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))
        Product.objects.bulk_create(product_for_create)

        data_version = Command.read_fixtures_json('catalog', '003_versions_data')
        version_for_create = []
        for version in data_version:
            version_for_create.append(Version(product=Product.objects.get(pk=version['fields']['product']),
                                              number_version=version['fields']['number_version'],
                                              title_version=version['fields']['title_version'],
                                              is_active=version['fields']['is_active'],
                                              ))
        Version.objects.bulk_create(version_for_create)

        data_articles = Command.read_fixtures_json('journal', '001_articles_data')
        article_for_create = []
        for article in data_articles:
            article_for_create.append(Articles(title=article['fields']['title'],
                                               slug=article['fields']['slug'],
                                               text=article['fields']['text'],
                                               image=article['fields']['image'],
                                               created_at=article['fields']['created_at'],
                                               flag_publication=article['fields']['flag_publication'],
                                               count_views=article['fields']['count_views'],
                                               ))
        Articles.objects.bulk_create(article_for_create)
