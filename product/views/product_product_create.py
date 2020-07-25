from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.forms.product_product import ProductForm


@login_required(login_url="/login/")
def product_create(request):
    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
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
