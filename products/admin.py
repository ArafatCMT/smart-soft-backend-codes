from django.contrib import admin
from .models import Category, Brand, Unit, Product
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ['owner','name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['owner','name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'category', 'brand', 'sale_price', 'purchase_cost']

class UnitAdmin(admin.ModelAdmin):
    list_display = ['owner','name']


admin.site.register(Unit)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)


