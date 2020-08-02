from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models.product_product import Product
from product.forms.product_product import ProductForm
from product.models.product_images import Images
from product.forms.product_images import ImageForm
from core.views.core_home import home
from django.forms import inlineformset_factory


@login_required(login_url="/login/")
def product_edit(request, id):
    product = Product.objects.get(id=id)
    images = Images.objects.filter(post=product)
    ImageFormSet = inlineformset_factory(
        Product, Images, fields=("image",))
    if request.method == "POST":
        if request.user == product.user:
            form = ProductForm(
                request.POST, 
                request.FILES, 
                instance=product
            )
            formset = ImageFormSet(
                request.POST, request.FILES, 
                instance=product)
            if formset.is_valid() and form.is_valid():
                form.save()
                formset.save()
                alert = "Вы изменили публикацию"
                return render(
                    request, "product/product.html",
                    {'alert': alert, 'product': product,
                    "images": images}
                )
        else:
            return redirect(home)
    else:
        if request.user == product.user:
            formset = ImageFormSet(instance=product)
            form = ProductForm(instance=product)
            message = "Редактировать публикацию"
        else:
            return redirect(home)
    return render(
        request, "product/form.html",
        {"form": form, 
        "formset": formset,
        "message": message}
    )
