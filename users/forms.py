from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, User
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """Настройка формы для регистрации с изменениями в HTML форме."""
    class Meta:
        model = CustomUser
        fields = ("photo", "username", "email", "first_name", "last_name",
                  "bio")
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Логин"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "first_name": forms.TextInput(attrs={"placeholder": "Имя"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Фамилия"}),
            "bio": forms.Textarea(
                attrs={'rows': 6, "placeholder": "Информация о себе"}
            ),
            "photo": forms.FileInput(
                attrs={"id": "imageUpload", "capture": ""}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Подтвердите пароль'})



class CustomUserChangeForm(UserChangeForm):
    """Настройка формы редактирования полей пользователя."""
    class Meta:
        model = CustomUser
        fields = ("photo", "username", "email", "first_name", "last_name",
                  "bio")


class LoginForm(AuthenticationForm):
    """Форма для авторизации пользователя по логину и паролю."""
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'placeholder': 'Логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
