from django.urls import path
from .views import SinghUpView, LoginUser


app_name = "users"

urlpatterns = [
    path("singup/", SinghUpView.as_view(), name="singup"),
    path("login/", LoginUser.as_view(), name="login"),
]
