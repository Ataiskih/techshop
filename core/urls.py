from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (home, profile_user, profile_edit, sellers)
from core.views.core_home import (blog, blog_details, check_out,
    contact, faq, index, login, main, product, register, shop,
    shopping_cart)


urlpatterns = [
    path("", home, name="home"),
    path("main/", index, name="index"),
    path("blog/", blog, name="blog"),
    path("blog_details/", blog_details, name="blog_details"),
    path("check_out/", check_out, name="check_out"),
    path("contacts/", contact, name="contact"),
    path("faq/", faq, name="faq"),
    path("logins/", login, name="logins"),
    path("8/", main, name="main"),
    path("9/", product, name="product"),
    path("register/", register, name="register"),
    path("shop/", shop, name="shop"),
    path("shopping_cart/", shopping_cart, name="shopping_cart"),


    path("profile/<int:pk>/", profile_user, name="profile"),
    path("profile_edit/<int:id>/", profile_edit, name="profile_edit"),
    path("sellers/", sellers, name="sellers"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
