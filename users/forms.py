from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Настройка формы для регистрации."""
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """Настройка формы редактирования полей пользователя."""
    class Meta:
        model = CustomUser
        fields = ("username", "email")
