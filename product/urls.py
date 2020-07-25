from django.urls import path
from product.views.product_product import product
from product.views.product_product_create import product_create
from product.views.product_product_delete import delete_post
from product.views.product_product_edit import product_edit
from product.views.product_products import products


urlpatterns = [
    path("all/", products, name="products"),
    path("<int:id>/", product, name="product"),
    path("create/", product_create, name="product-create"),
    path("edit/<int:id>/", product_edit, name="product-edit"),
    path("delete/<int:id>/", delete_post, name="product-delete"),
]
