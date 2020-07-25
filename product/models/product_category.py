from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
