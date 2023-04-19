from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from users.models import Notification, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    """Добавление в админку сайта собственной модели и форму регистрации
       пользователей, настройка отображения полей в админке.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (None, {"fields": ("photo", "bio", "notifications")})
    )
    list_display = ("username", "email", "get_bio", "get_html_photo",
                    "get_notifications")
    search_fields = ("username", "email")

    def get_bio(self, obj):
        """
        Если биография длиннее 100 символов - возвращает обрезанную версию.
        """
        if len(obj.bio) > 100:
            return mark_safe(f"{obj.bio[:100]}...")
        return obj.bio

    def get_html_photo(self, obj):
        """
        Проверяет есть ли фото, если есть - возвращает HTML элемент
        для отображения миниатюры.
        """
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")
        else:
            return "-"

    def get_notifications(self, obj):
        """
        Выводит все уведомления, на которые подписан пользователь.
        """
        return ", ".join([x.notification for x in obj.notifications.all()])

    # Замена заголовков у полей получаемых через функцию:
    get_notifications.short_description = "Уведомления"
    get_html_photo.short_description = "Миниатюра"
    get_bio.short_description = "Биография"


class NotificationsAdmin(admin.ModelAdmin):
    """
    Кастомизация полей админки для модели уведомлений.
    """
    list_display = ("notification", "slug")
    prepopulated_fields = {"slug": ("notification",)}


admin.site.register(Notification, NotificationsAdmin)
admin.site.register(CustomUser, CustomUserAdmin)


