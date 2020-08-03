from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.forms.core_change_password import MyCustomChangePasswordForm
# from core.views.core_profile import profile_user


@login_required(login_url="/login/")
def profile_edit(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST" and "edit_profile" in request.POST:
        if request.user != user:
            return redirect(home)
        else:
            form = ChangePersonalInfo(
                request.POST,
                instance=user)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Вы изменили персональную информацию'
                )
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
                user.email = new_email
                user.save()
                messages.success(request, 'Вы сменили email')
                return HttpResponseRedirect(
                    request.path_info
                )
            else:
                messages.success(request, 'Вы ввели не верный email')
                return HttpResponseRedirect(
                    request.path_info
                )
    elif request.method == "POST" and "change_password" in request.POST:
        if request.user != user:
            return redirect(home)
        else:
            # вариант с стандартой формой
            # form = auth.forms.PasswordChangeForm(
            #     data=request.POST,
            #     user=request.user)
            # if form.is_valid():
            #     form.save()
            #     auth.update_session_auth_hash(
            #         request, form.user)
            #     # messages.success(request, 'Ваш пароль был успешно изменен')
            #     return redirect('profile_user', id=user.id)
            form = MyCustomChangePasswordForm(
                data=request.POST,
                user=request.user
            )
            if form.is_valid():
                form.save()
                return redirect(home)
    elif request.method == "GET":
        if request.user == user:
            return render(
                request,
                "core/profile_edit.html",
                {'user': user,
                 "form": auth.forms.PasswordChangeForm(user=user)}
            )
        else:
            return redirect(home)
