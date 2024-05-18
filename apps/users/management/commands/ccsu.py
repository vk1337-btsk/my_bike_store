import configparser
import os

from django.core.management import BaseCommand

from apps.users.models import User
from config.settings import BASE_DIR

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, "config.ini"))


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=config['data_admin']['ADMIN_EMAIL'],
            first_name='Admin',
            last_name='Roots',
            is_staff=True,
            is_superuser=True
        )
        user.set_password(config['data_admin']['ADMIN_PASSWORD'])
        user.save()
