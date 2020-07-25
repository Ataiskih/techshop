from django.urls import path
from core.views.core_home import home
from core.views.core_profile import profile_user
from core.views.core_profile_edit import profile_edit
from core.views.core_sellers import sellers


urlpatterns = [
    path("", home, name="home"),
    path("profile/<int:pk>/", profile_user, name="profile"),
    path("profile_edit/<int:id>/", profile_edit, name="profile_edit"),
    path("sellers/", sellers, name="sellers"),
]
