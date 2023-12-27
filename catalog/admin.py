from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price_for_one', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
