from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models.product_product import Product


@login_required(login_url="/login/")
def delete_post(request, id):
    if request.method == 'POST':
        post = Product.objects.get(pk=id)
        post.deleted = True
        post.save()
        alert = "Вы удалили публикацию"
        return render(
            request,
            "product/products.html",
            {'alert': alert})
    return render(request, 'product/product.html')
