from django.db import models
from django.contrib.auth.models import User


class Images(models.Model):
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_images",
        verbose_name="дополнительные изображения товаров"
    )
