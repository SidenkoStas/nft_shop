from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login
from users.models import CustomUser


class SinghUpView(CreateView):
    model = CustomUser
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("shop:index")

    def form_valid(self, form):
        valid = super(SinghUpView, self).form_valid(form)
        form.save_m2m()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class LoginUser(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm


class ProfileView(DetailView):
    model = CustomUser
    template_name = "users/profile.html"

