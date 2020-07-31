from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.forms.product_product import ProductForm
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from product.forms.product_images import ImageForm
from product.models.product_images import Images
from core.views.core_home import home

@login_required(login_url="/login/")
def product_create(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
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
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(image=image)
                    photo.save()
            # use django messages framework
            # alert = "Товар был добавлен успешно!"
            # return render(
            #     request,
            #     "product/products.html",
            #     {"alert": alert}
            # )
            return redirect(home)
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
