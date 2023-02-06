from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


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

    def get_absolute_url(self):
        return reverse("")


class Item(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Цена")
    artist = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name="Художник")
    image = models.ImageField(upload_to="nft/%Y/%m/%d/", verbose_name="NFT")
    likes = models.ImageField(verbose_name="Лайки")
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


class HistoryNft(models.Model):
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")
    nft = models.ForeignKey(to=Item, on_delete=models.PROTECT,
                            verbose_name="NFT")
    buyers = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name="Покупатель")
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "История NFT"
        verbose_name_plural = "Истории NFT"
        ordering = ["-purchase_date"]

    def __str__(self):
        return f"{self.nft} - {self.buyers}"


class Bits(models.Model):
    slug = models.SlugField(max_length=250, unique=True, db_index=True,
                            verbose_name="Slug")
    buyers = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name="Покупатель")
    nft = models.ForeignKey(to=Item, on_delete=models.PROTECT,
                            verbose_name="NFT")
    bit = models.DecimalField(max_digits=7, decimal_places=4,
                              verbose_name="Ставка")

    class Meta:
        verbose_name = "Ставка"
        verbose_name_plural = "Ставки"

    def __str__(self):
        return f"{self.buyers} - {self.bit}"
