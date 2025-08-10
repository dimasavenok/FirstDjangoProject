from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаление старых данных...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Загрузка данных из фикстуры...")
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')

        self.stdout.write(self.style.SUCCESS("Тестовые данные загружены из фикстуры"))

