from django.shortcuts import render
from stocks.models import Stock
from rest_framework.generics import ListAPIView
from rest_framework import filters
from . import serializers
from rest_framework.views import APIView
from products.models import Product
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class ShowStock(filters.BaseFilterBackend):#
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset
    
class ShowStockView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = serializers.StockSerializer
    filter_backends = [ShowStock]

class CheckStockView(APIView):
    serializer_class = serializers.StockSerializer

    def get_objects(self, id):
        try:
            return Product.objects.get(id=id)
        except(Product.DoesNotExist):
            return None
        
    def get(self, request, id, format=None):
        product = self.get_objects(id)
        if product:
            stock = Stock.objects.get(product=product)
            serializer = serializers.StockSerializer(stock)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
