from django.db import models

from usersapp.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя категории")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
        ('unpublished', 'Снято с публикации'),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя продукта")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)


    def __str__(self):
        return f"{self.name} | {self.category} | {self.price}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "Разрешение на удаление любого продукта")
        ]
