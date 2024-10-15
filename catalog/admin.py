from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')  # Отображаемые поля
    search_fields = ('name', 'category')  # Поля для поиска

admin.site.register(Product, ProductAdmin)
