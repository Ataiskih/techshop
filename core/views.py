from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.models import Product


def home(request):
    return redirect("products")


@login_required(login_url="/login/")
def profile(request):
    products = Product.objects.filter(
        availability_in_store=True,
        user=request.user
    )
    return render(
        request, 
        "core/profile.html",
        {"products": products}
    )
