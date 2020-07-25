from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product",
        verbose_name="Автор"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_image",
        verbose_name="изображение товара",
        default="static/no_image.png"
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
        verbose_name="колличество в магазине"
    )
    availability_in_store = models.BooleanField(
        default=True,
        verbose_name="наличие в магазине"
    )
    deleted = models.BooleanField(
        default=False,
        verbose_name="Скрыт от пользователей"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["name"]
