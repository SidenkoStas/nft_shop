from django.db import models
from django.urls import reverse


class Category(models.Model):
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
    title = models.CharField(max_length=150, verbose_name="Коллекция")
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Item(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Цена")
    artist = models.CharField(max_length=150, verbose_name="Художник")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="NFT")
    category = models.ForeignKey(to="Category", on_delete=models.PROTECT,
                                 verbose_name="Категория")
    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Дата создания")
    collections = models.ManyToManyField("Collections", blank=True,
                                         verbose_name="Коллекции")

    class Meta:
        verbose_name = "NFT token"
        verbose_name_plural = "NFT tokens"
        ordering = ["-creation_date", "title"]

    def get_absolute_url(self):
        return reverse("shop:index")

    def __str__(self):
        return f"{self.title}"
