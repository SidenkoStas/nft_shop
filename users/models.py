from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Notification(models.Model):
    """Модель уведомлений, меняется только админом."""
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
    """Своя модель пользователей с основой от Django."""
    photo = models.ImageField(
        upload_to="profile_photos/%Y/%m/%d/", blank=True, null=True,
        default="default.png",
        verbose_name="Фото профиля"
    )
    bio = models.TextField(blank=True, verbose_name="Биография")
    notifications = models.ManyToManyField(
        Notification, blank=True, verbose_name="Уведомления"
    )

    def get_notifications(self):
        return "\n".join([p.notifications for p in self.notifications.all()])

    def get_absolute_url(self):
        return reverse("user")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}"
