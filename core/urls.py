from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (home, profile_user, profile_edit, sellers)


urlpatterns = [
    path("", home, name="home"),
    path("profile/<int:pk>/", profile_user, name="profile"),
    path("profile_edit/<int:id>/", profile_edit, name="profile_edit"),
    path("sellers/", sellers, name="sellers"),
]
