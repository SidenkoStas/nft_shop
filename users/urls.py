from django.urls import path
from .views import SinghUpView, LoginUser, ProfileView, UpdateProfileView
from django.contrib.auth.views import LogoutView


app_name = "users"

urlpatterns = [
    path("signup/", SinghUpView.as_view(), name="signup"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("edit_profile/<int:pk>", UpdateProfileView.as_view(),
         name="edit_profile"),
]
