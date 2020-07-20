from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.models import Product


def home(request):
    return redirect("products")


@login_required(login_url="/login/")
def profile_user(request, pk):
    user = User.objects.get(pk=pk)
    return render(
        request,
        "core/profile.html",
        {'user': user}
    )


def sellers(request):
    # исключение у кого товаров нет:
    # или products = Products.objects.all()
    # User.objects.filter(product__in=products).distinct()
    sellers = User.objects.exclude(
        product=None
    )
    return render(
        request, "core/sellers.html",
        {"sellers": sellers}
    )
