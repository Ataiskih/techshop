from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import Product
from product.forms import ProductForm


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


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # message = "Автор был добавлен успешно!"
            return redirect(products)
    elif request.method == "GET":
        form = ProductForm()
        return render(
            request, "product/form.html",
            {"form": form}
        )


def product_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        form = ProductForm(
            request.POST,
            instance=product
        )
        if form.is_valid():
            form.save()
            # message = "Автор был добавлен успешно!"
            return redirect("product", id=product.id)
    elif request.method == "GET":
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        return render(
            request, "product/form.html",
            {"form": form}
        )