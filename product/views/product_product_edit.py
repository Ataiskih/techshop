from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models.product_product import Product
from product.forms.product_product import ProductForm
from product.models.product_images import Images
from product.forms.product_images import ImageForm
from core.views.core_home import home
from django.forms import modelformset_factory


@login_required(login_url="/login/")        # проверка авториз
def product_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if request.user != product.user:
            return redirect("home")
        else:
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
        images = Images.objects.filter(post=product)
        ImageFormSet = modelformset_factory(
            Images, form=ImageForm)
        if request.user != product.user:
            return redirect("home")
        else:
            form = ProductForm(instance=product)
            formset = ImageFormSet(queryset=images)
            message = "Редактировать публикацию"
            return render(
                request, "product/form.html",
                {"form": form, 
                "formset": formset,
                "message": message}
            )
