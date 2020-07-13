from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import Product, Category
from product.forms import ProductForm
from django.db.models import Q 


def products(request):
    if "key_word" in request.GET:
        key = request.GET.get("key_word")
        products = Product.objects.filter(Q(availability_in_store=True),
            Q(name__icontains=key) |
            Q(description__icontains=key) |
            Q(category__name__contains=key)
        )
        products = products.distinct()
    else:
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
        form = ProductForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            alert = "Товар был добавлен успешно!"
            return render(
                request,
                "product/products.html",
                {"alert": alert}
            )
    elif request.method == "GET":
        form = ProductForm()
        message = "Добавить товар"
        return render(
            request, 
            "product/form.html",
            {"form": form, "message": message}
        )


def product_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )
        if form.is_valid():
            form.save()
            return redirect(
                "product", id=product.id
            )
    elif request.method == "GET":
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        message = "Редактировать публикацию"
        return render(
            request, "product/form.html",
            {"form": form, "message": message}
        )
