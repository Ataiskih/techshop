from django.shortcuts import render
from django.db.models import Q
from product.models.product_product import Product


def products(request):
    if "key_word" in request.GET:
        key = request.GET.get("key_word")
        products = Product.objects.filter(
            Q(availability_in_store=True),
            Q(deleted=False),
            Q(name__contains=key) |
            Q(description__contains=key) |
            Q(category__name__contains=key)
        )
        products = products.distinct()
    else:
        products = Product.objects.filter(
            # availability_in_store=True,
            deleted=False
        )
    return render(
        request, "product/products.html",
        {"products": products})
