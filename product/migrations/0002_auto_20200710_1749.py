# Generated by Django 3.0.8 on 2020-07-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability_in_store',
            field=models.BooleanField(default=True, verbose_name='наличие в магазине'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_purchases',
            field=models.IntegerField(default=0, verbose_name='колличество продаж'),
        ),
    ]
