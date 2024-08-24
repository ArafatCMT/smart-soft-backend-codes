from rest_framework import serializers
from products import models

class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Category
        fields = ['id', 'owner', 'name']
        read_only_fields = ['owner']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ['id','owner', 'name']
        read_only_fields = ['owner']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ['id', 'owner', 'name']
        read_only_fields = ['owner']


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    # owner = serializers.StringRelatedField(many=False)
    # brand = serializers.StringRelatedField(many=False)
    # unit = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Product
        fields = ['owner', 'name', 'category', 'brand', 'unit', 'sale_price', 'purchase_cost']
        read_only_fields = ['owner']
