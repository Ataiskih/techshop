from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.models import Product
from core.forms import MyCustomChangePasswordForm, \
    ChangePersonalInfo



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
    if request.method == "POST" and "change_password" in request.POST:
        if request.user != user:
            return redirect(home)
        else:
            form = MyCustomChangePasswordForm(
                request.POST
            )
            if form.is_valid():
                form.save()
            # password_1 = request.POST.get("password1")
            # password_2 = request.POST.get("password2")
            # form = MyCustomChangePasswordForm(
            #     request.POST
            # )
            # if password_1 == password_2:
            #     user.set_password(password_1)
            #     user.save()
                return HttpResponseRedirect(
                    request.path_info
                )
    elif request.method == "POST" and "edit_profile" in request.POST:
        if request.user != user:
            return redirect(home)
        else:
            form = ChangePersonalInfo(
                request.POST,
                instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(
                    request.path_info
                )
    elif request.method == "POST" and "change_email" in request.POST:
        if request.user != user:
            return redirect(home)
        else:
            user = request.user
            old_email = request.POST.get("old_email")
            new_email = request.POST.get("new_email")
            if user.email == old_email:
                new_email = user.email
                user.save()
                print(user.email)
                return HttpResponseRedirect(
                    request.path_info
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
