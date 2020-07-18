from django.urls import path
from core.views import home, profile_user


urlpatterns = [
    path("", home, name="home"),
    path("profile/<int:pk>/", profile_user, name="profile"),
]
