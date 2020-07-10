from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
        blank=True,
        verbose_name="категория"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="описание"
    )
    price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name="цена"
    )
    quantity_purchases = models.IntegerField(
        default=0,
        verbose_name="колличество продаж"
    )
    availability_in_store = models.BooleanField(
        default=True,
        verbose_name="наличие в магазине"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["name"]


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
