from django.shortcuts import render
from django.views.generic import DetailView
from product.models.product_product import Product
from product.models.product_images import Images


class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product

    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        product = Product.objects.get(id=pk)
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=pk)
        context['images'] = Images.objects.filter(post=product)
        return context


# # Вариант 2 с использованием функций
# def product(request, id):
#     product = Product.objects.get(id=id)
#     images = Images.objects.filter(post=product)
#     return render(
#         request, "product/product.html",
#         {"product": product, 'images': images}
#     )
