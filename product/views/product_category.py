from django.shortcuts import render
from django.views.generic import DetailView
from product.models.product_product import Product


class CategoryDetailView(DetailView):
    template_name = "product/products.html"
    model = Product

    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category__id=pk,
            # availability_in_store=True,
            deleted=False
        )
        category_pk = pk
        return context


# # Вариант 2 с использованием функций
# def category(request, pk):
#     products = Product.objects.filter(
#         category__id=pk,
#         # availability_in_store=True,
#         deleted=False
#     )
#     category_pk = pk
#     return render(
#         request, "product/products.html",
#         {"products": products, 
#         "category_pk": category_pk}
#     )
