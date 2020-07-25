from django.shortcuts import render
from django.contrib.auth.models import User
from product.models import Product


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
