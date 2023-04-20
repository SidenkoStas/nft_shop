from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login
from users.models import CustomUser


class SinghUpView(CreateView):
    """
    Представление для управления регистрацией новых пользователей.
    """
    model = CustomUser
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("shop:index")

    def form_valid(self, form):
        """
        Функция автоматической авторизации пользователя после регистрации.
        Сохраняет информацию в поля многие ко многим.
        """
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

    def get_context_data(self, **kwargs):
        """
        Добавляем все токены, связанные с профилем + счётчик токенов.
        """
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.artist.all()
        context["total_items"] = self.object.artist.all().count()
        return context


class UpdateProfileView(UpdateView):
    model = CustomUser
    success_url = reverse_lazy("shop:index")
    template_name = "users/edit_profile.html"
    fields = ["photo", "username", "email", "first_name", "last_name", "bio",
              "notifications"]

    # def form_valid(self, form):
    #     """
    #     Функция автоматической авторизации пользователя после регистрации.
    #     Сохраняет информацию в поля многие ко многим.
    #     """
    #     valid = super(UpdateProfileView, self).form_valid(form)
    #     form.save_m2m()
    #     return valid
