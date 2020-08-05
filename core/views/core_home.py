from django.shortcuts import redirect, render


def home(request):
    return redirect("products")


def blog(request):
    return render(request, "fashi/blog.html")

def blog_details(request):
    return render(request, "fashi/blog-details.html")

def check_out(request):
    return render(request, "fashi/check-out.html")

def contact(request):
    return render(request, "fashi/contact.html")

def faq(request):
    return render(request, "fashi/faq.html")

def index(request):
    return render(request, "fashi/index.html")

def login(request):
    return render(request, "fashi/login.html")

def main(request):
    return render(request, "fashi/main.html")

def product(request):
    return render(request, "fashi/product.html")

def register(request):
    return render(request, "fashi/register.html")

def shop(request):
    return render(request, "fashi/shop.html")

def shopping_cart(request):
    return render(request, "fashi/shopping-cart.html")