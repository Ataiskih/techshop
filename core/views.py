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
