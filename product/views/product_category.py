from django.shortcuts import render
from product.models.product_product import Product



def category(request, pk):
    products = Product.objects.filter(
        category__id=pk,
        # availability_in_store=True,
        deleted=False
    )
    category_pk = pk
    return render(
        request, "product/products.html",
        {"products": products, 
        "category_pk": category_pk}
    )
