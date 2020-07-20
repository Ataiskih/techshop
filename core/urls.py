from django.urls import path
from core.views import home, profile_user, \
    sellers


urlpatterns = [
    path("", home, name="home"),
    path("profile/<int:pk>/", profile_user, name="profile"),
    path("sellers/", sellers, name="sellers"),
]
