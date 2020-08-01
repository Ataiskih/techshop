from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib import messages
from product.views.product_product import product
from product.forms.product_product import ProductForm
from product.forms.product_images import ImageForm
from product.models.product_images import Images


@login_required(login_url="/login/")
def product_create(request):
    ImageFormSet = modelformset_factory(
        Images, form=ImageForm, extra=6)
    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES
        )
        formset = ImageFormSet(
            request.POST, request.FILES,
            queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(
                        post=new_product,
                        image=image
                    )
                    photo.save()
            messages.success(
                request, 
                'Товар был добавлен успешно!')
            return redirect('/product/all/')
    elif request.method == "GET":
        form = ProductForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        message = "Добавить товар"
        return render(
            request,
            "product/form.html",
            {"form": form,
            "formset": formset,
            "message": message}
        )
