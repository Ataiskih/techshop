from django.db import models
from product.models.product_product import Product


class Images(models.Model):
    post = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="images"
        )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_images",
        verbose_name="дополнительные изображения товаров"
    )

    class Meta:
        verbose_name = "Дополнительные фотографии"
        verbose_name_plural = "Дополнительные фотографии"
