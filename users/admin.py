from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from users.models import Notification, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    """Добавление в админку сайта собственной модели и форм регистрации
       пользователей, настройка отображения полей в админке.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "bio", "get_html_photo",
                    "get_notifications")
    search_fields = ("username", "email")

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    def get_notifications(self, obj):
        if obj.notifications:
            return "Нет уведомлений"
        return obj.notifications

    get_notifications.short_description = "Уведомления"
    get_html_photo.short_description = "Миниатюра"


class NotificationsAdmin(admin.ModelAdmin):
    """Кастомизация полей админки для модели уведомлений."""
    list_display = ("notification", "slug")
    prepopulated_fields = {"slug": ("notification",)}


admin.site.register(Notification, NotificationsAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_title = "Коллекционирование и продажа NFT"
admin.site.site_header = "Коллекционирование и продажа NFT"
