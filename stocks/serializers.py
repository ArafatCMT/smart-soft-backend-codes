from rest_framework import serializers
from stocks import models

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        fields = ['owner', 'product', 'purchase', 'sold', 'available_stock', 'sale_value', 'purchase_value']
        read_only_fields = ['owner']