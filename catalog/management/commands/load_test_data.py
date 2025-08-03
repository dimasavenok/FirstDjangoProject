from django.core.management.base import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Load test data'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        cat = Category.objects.create(name="cat1", description="d")
        for i in range(6):
            Product.objects.create(name=f"p{i}", description="pd", category=cat, price=1.11*(i+1))
        self.stdout.write(self.style.SUCCESS("Тестовые продукты загружены"))

