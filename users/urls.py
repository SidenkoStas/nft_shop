from django.urls import path
from .views import SinghUpView, LoginUser


app_name = "users"

urlpatterns = [
    path("signup/", SinghUpView.as_view(), name="signup"),
    path("login/", LoginUser.as_view(), name="login"),
]
