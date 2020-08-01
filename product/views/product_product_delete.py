from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product.models.product_product import Product


@login_required(login_url="/login/")
def delete_post(request, id):
    if request.method == 'POST':
        post = Product.objects.get(pk=id)
        post.deleted = True
        post.save()
        messages.success(
            request, 
            'Вы удалили публикацию')
        return redirect('/product/all/')
    return render(request, 'product/product.html')
