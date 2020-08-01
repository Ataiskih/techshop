from django.shortcuts import render
from product.models.product_product import Product
from product.models.product_images import Images


def product(request, id):
    product = Product.objects.get(id=id)
    images = Images.objects.filter(post=product)
    return render(
        request, "product/product.html",
        {"product": product, 'images': images}
    )
