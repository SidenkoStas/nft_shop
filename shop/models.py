from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from likes.models import Like

User = get_user_model()


class Category(models.Model):
    """
    Модель категорий для NFT токенов.
    """
    title = models.CharField(max_length=50, verbose_name="Категории")
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Collections(models.Model):
    """
    Модель для коллекций NFT токенов, не относится к категориям.
    """
    title = models.CharField(max_length=150, verbose_name="Коллекция")
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("")


class Item(models.Model):
    """
    Модель NFT токенов.
    """
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Цена")
    artist = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name="Художник", related_name="artist")
    image = models.ImageField(upload_to="nft/%Y/%m/%d/", verbose_name="NFT")
    category = models.ForeignKey(to="Category", on_delete=models.PROTECT,
                                 verbose_name="Категория")
    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Дата создания")
    collections = models.ManyToManyField("Collections", blank=True,
                                         verbose_name="Коллекции")
    likes = GenericRelation(Like)

    class Meta:
        verbose_name = "NFT токен"
        verbose_name_plural = "NFT токены"
        ordering = ["-creation_date", "title"]

    @property
    def total_likes(self):
        return f"{self.likes.count()}"

    def get_absolute_url(self):
        return reverse("shop:index")

    def __str__(self):
        return f"{self.title}"


class OwnerNFT(models.Model):
    """
    Владельцы создавшие токены или купившего.
    """
    owner = models.ForeignKey(User, on_delete=models.PROTECT,
                              verbose_name="Владелец", related_name="owner")
    item = models.ManyToManyField("Item", verbose_name="NFT токен")

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

    def __str__(self):
        return f"{self.owner} - {self.item}"
