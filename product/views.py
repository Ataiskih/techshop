from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import Product


def products(request):
    products = Product.objects.filter(
        availability_in_store=True)
    return render(
        request, "product/products.html",
        {"products": products})


def product(request, id):
    product = Product.objects.get(id=id)
    return render(
        request, "product/product.html",
        {"product": product}
    )
