from django.contrib import admin
from .models import Purchase, Sale
# Register your models here.
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['owner', 'supplier', 'product', 'purchase_date', 'quentity', 'payable', 'paid', 'due']


class SaleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'customer', 'product', 'quentity', 'date', 'receivable', 'paid', 'due', 'purchase_cost', 'profit', 'status']

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sale, SaleAdmin)
