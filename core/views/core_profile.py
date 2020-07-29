from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.models.product_category import Category


@login_required(login_url="/login/")
def profile_user(request, pk):
    user = User.objects.get(pk=pk)
    category_count = Category.objects.filter(
        product__in=user.product.all()
    ).distinct().count()
    return render(
        request,
        "core/profile.html",
        {'user': user,
        "category_count": category_count}
    )
