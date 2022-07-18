from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="category")

    def __str__(self):
        return f"{self.title}"


class Item(models.Model):
    title = models.CharField(max_length=150, verbose_name="item_name")
    description = models.TextField(verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, verbose_name="category")

    def __str__(self):
        return f"{self.title}"
