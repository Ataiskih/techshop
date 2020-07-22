from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.models import Product
from core.forms import UserForm


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


@login_required(login_url="/login/")
def profile_edit(request,id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        if request.user != user:
            return redirect(home)
        else:
            form = UserForm(
            request.POST,
            instance=user
        )
        if form.is_valid():
            form.save()
            return render(
                request,
                "core/profile_edit.html",
                {'user': user}
            )
    elif request.method == "GET":
        if request.user == user:
            return render(
                request,
                "core/profile_edit.html",
                {'user': user}
        )
        else:
            return redirect(home)


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
