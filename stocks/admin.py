from django.contrib import admin
from stocks.models import Stock

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ['owner','product', 'category', 'price', 'cost', 'purchase', 'unit', 'sold', 'available_stock', 'sale_value', 'purchase_value']

    def product(self, obj):
        return f"{obj.product.name}"
    
    def category(self, obj):
        return f"{obj.product.category}"
    
    def price(self, obj):
        return f"{obj.product.sale_price}"
    
    def cost(self, obj):
        return f"{obj.product.purchase_cost}"
    
    def unit(self, obj):
        return f"{obj.product.unit}"


admin.site.register(Stock, StockAdmin)
