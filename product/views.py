from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, "product/products.html", {"products": products})
