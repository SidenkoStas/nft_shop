from django.contrib import admin
from shop.models import Category, Item
from django.utils.safestring import mark_safe


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "get_html_item", "creation_date")
    prepopulated_fields = {"slug": ("title",)}

    def get_html_item(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width=50>")

    get_html_item.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
