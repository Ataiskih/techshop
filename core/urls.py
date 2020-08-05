from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (home, profile_user, profile_edit, sellers)
from core.views.core_home import (blog, blog_details, check_out,
    contact, faq, index, login, main, product, register, shop,
    shopping_cart)


urlpatterns = [
    path("", home, name="home"),
    path("1/", index, name="index"),
    path("2/", blog, name="blog"),
    path("3/", blog_details, name="blog_details"),
    path("4/", check_out, name="check_out"),
    path("5/", contact, name="contact"),
    path("6/", faq, name="faq"),
    path("7/", login, name="login"),
    path("8/", main, name="main"),
    path("9/", product, name="product"),
    path("10/", register, name="register"),
    path("11/", shop, name="shop"),
    path("12/", shopping_cart, name="shopping_cart"),


    path("profile/<int:pk>/", profile_user, name="profile"),
    path("profile_edit/<int:id>/", profile_edit, name="profile_edit"),
    path("sellers/", sellers, name="sellers"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
