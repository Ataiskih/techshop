from django.shortcuts import render
from product.models.product_product import Product
from product.models.product_category import Category


def product(request, id):
    product = Product.objects.get(id=id)
    return render(
        request, "product/product.html",
        {"product": product}
    )
