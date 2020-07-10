from django.urls import path
from product.views import products, product


urlpatterns = [
    path("all/", products, name="products"),
    path("<int:id>/", product, name="product"),
]
