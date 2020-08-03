from django.urls import path
from product.views import (
    CategoryDetailView, ProductDetailView,
    ProductCreate, delete_post, product_edit, products
    )


urlpatterns = [
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("create/", ProductCreate.as_view(), name="product-create"),
    path("delete/<int:id>/", delete_post, name="product-delete"),
    path("edit/<int:id>/", product_edit, name="product-edit"),
    path("all/", products, name="products"),
]
