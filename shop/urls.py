from django.urls import path
from .views import index, profile, ProfileView


app_name = "shop"

urlpatterns = [
    path("", index, name="index"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
