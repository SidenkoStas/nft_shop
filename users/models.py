from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Notification(models.Model):
    """
    Модель уведомлений для рассылки пользователям,
    меняется только админом.
    """
    slug = models.SlugField(
        max_length=250, unique=True, db_index=True, verbose_name="Slug"
    )
    notification = models.CharField(max_length=150, verbose_name="Уведомления")

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self):
        return f"{self.notification}"



class CustomUser(AbstractUser):
    """
    Своя модель пользователей которая расширяет модель от Django.
    """
    photo = models.ImageField(
        upload_to="profile_photos/%Y/%m/%d/", blank=True, null=True,
        default="default.png",
        verbose_name="Фото профиля"
    )
    bio = models.TextField(blank=True, verbose_name="Биография")
    notifications = models.ManyToManyField(
        Notification, blank=True, verbose_name="Уведомления",
        related_name="notifications",

    )

    def get_notifications(self):
        """
        Возвращает список уведомлений к которым подписан пользователь.
        """
        return "\n".join([p.notification for p in self.notifications.all()])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}"
