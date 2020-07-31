# Generated by Django 3.0.8 on 2020-07-29 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='дополнительные изображения товаров')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.Images', verbose_name='категория'),
        ),
    ]