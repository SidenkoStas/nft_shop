from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, LoginForm


class SinghUpView(CreateView):
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class LoginUser(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm
