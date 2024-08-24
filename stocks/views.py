from django.shortcuts import render
from stocks.models import Stock
from rest_framework.generics import ListAPIView
from rest_framework import filters
from . import serializers
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