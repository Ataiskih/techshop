from django.shortcuts import render
from product.models.product_product import Product


def product(request, id):
    product = Product.objects.get(id=id)
    return render(
        request, "product/product.html",
        {"product": product}
    )
