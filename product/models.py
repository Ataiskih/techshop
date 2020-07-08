from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    quantity_purchases = models.IntegerField(default=0)
    availability_in_store = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["name"]
