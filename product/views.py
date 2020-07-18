from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, \
    user_passes_test
from django.db.models import Q
from product.models import Product, Category
from product.forms import ProductForm


def products(request):
    if "key_word" in request.GET:
        key = request.GET.get("key_word")
        products = Product.objects.filter(
            Q(availability_in_store=True),
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


@login_required(login_url="/login/")
def product_create(request):
    if request.method == "POST":
        form = ProductForm( 
            request.POST,
            request.FILES
        )
        if form.is_valid():
            new_product = form.save()
            new_product.user =request.user
            new_product.save()
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


@login_required(login_url="/login/")        # проверка авториз
def product_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if request.user != product.user:
            return redirect("home")
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )
        if form.is_valid():
            form.save()
            alert = "Вы изменили публикацию"
            return render(
                request, "product/product.html",
                {'alert': alert, 'product': product}
            )
    elif request.method == "GET":
        product = Product.objects.get(id=id)
        if request.user != product.user:
            return redirect("home")
        form = ProductForm(instance=product)
        message = "Редактировать публикацию"
        return render(
            request, "product/form.html",
            {"form": form, "message": message}
        )


@login_required(login_url="/login/")
def delete_post(request, id):
    if request.method == 'POST':
        post = Product.objects.get(pk=id)
        post.availability_in_store = False
        post.save()
        return redirect('products')
    return render(request, 'product/product.html')
