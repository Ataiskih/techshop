from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.forms.product_product import ProductForm
from product.forms.product_images import ImageForm
from product.models.product_images import Images
from product.models.product_product import Product


class ProductCreate(TemplateView, LoginRequiredMixin):
    login_url = "/login/"
    template_name = "product/form.html"

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        ImageFormSet = modelformset_factory(
            Images, form=ImageForm, extra=6)
        formset = ImageFormSet(queryset=Images.objects.none())
        message = "Добавить товар"
        context = {
            "form": form,
            "formset": formset,
            "message": message}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        ImageFormSet = modelformset_factory(
            Images, form=ImageForm, extra=6)
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
                    photo = Images(post=new_product, image=image)
                    photo.save()
            messages.success(
                request,
                'Товар был добавлен успешно!')
            return redirect('/product/all/')
        context = {"form": form, "formset": formset}
        return self.render_to_response(context)


# # Вариант 2 с использованием функций
# @login_required(login_url="/login/")
# def product_create(request):
#     ImageFormSet = modelformset_factory(
#         Images, form=ImageForm, extra=6)
#     if request.method == "POST":
#         form = ProductForm(
#             request.POST,
#             request.FILES
#         )
#         formset = ImageFormSet(
#             request.POST, request.FILES,
#             queryset=Images.objects.none())
#         if form.is_valid() and formset.is_valid():
#             new_product = form.save(commit=False)
#             new_product.user = request.user
#             new_product.save()
#             for form in formset.cleaned_data:
#                 if form:
#                     image = form['image']
#                     photo = Images(
#                         post=new_product,
#                         image=image
#                     )
#                     photo.save()
#             messages.success(
#                 request,
#                 'Товар был добавлен успешно!')
#             return redirect('/product/all/')
#     elif request.method == "GET":
#         form = ProductForm()
#         formset = ImageFormSet(queryset=Images.objects.none())
#         message = "Добавить товар"
#         return render(
#             request,
#             "product/form.html",
#             {"form": form,
#                 "formset": formset,
#                 "message": message}
#         )
