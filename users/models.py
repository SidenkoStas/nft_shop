from django.db import models
from django.contrib.auth.models import AbstractUser


class Notification(models.Model):
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")
    notification = models.CharField(max_length=150, verbose_name="Уведомления")

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self):
        return f"{self.notification}"


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile_photos/%Y/%m/%d/", blank=True,
                              verbose_name="Фото профиля")
    bio = models.TextField(verbose_name="Биография")
    vk_links = models.CharField(max_length=150,
                                verbose_name="Ссылка на ВКонтакте")
    notifications = models.ManyToManyField(Notification, blank=True,
                                           verbose_name="Уведомления")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}"
