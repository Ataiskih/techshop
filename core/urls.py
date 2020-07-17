from django.urls import path
from core.views import home, profile


urlpatterns = [
    path("", home, name="home"),
    path("profile/", profile, name="profile"),
]
