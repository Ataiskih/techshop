from django import forms
from product.models.product_product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", "image", "category", "description", "price",
            "availability_in_store", "deleted"
        ]
