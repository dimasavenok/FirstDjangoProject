from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = "Создаёт группы Модератор продуктов и Контент-менеджер"

    def handle(self, *args, **kwargs):
        product_ct = ContentType.objects.get_for_model(Product)

        # Создаём группу "Модератор продуктов"
        moderator_group, created = Group.objects.get_or_create(name="Модератор продуктов")
        if created:
            self.stdout.write(self.style.SUCCESS("Группа 'Модератор продуктов' создана"))

        # Права: удаление продукта + can_unpublish_product
        delete_perm = Permission.objects.get(codename="delete_product", content_type=product_ct)
        unpublish_perm = Permission.objects.get(codename="can_unpublish_product", content_type=product_ct)

        moderator_group.permissions.add(delete_perm, unpublish_perm)
        self.stdout.write(self.style.SUCCESS("Права добавлены группе 'Модератор продуктов'"))

        # Создаём группу "Контент-менеджер"
        content_manager_group, created = Group.objects.get_or_create(name="Контент-менеджер")
        if created:
            self.stdout.write(self.style.SUCCESS("Группа 'Контент-менеджер' создана"))