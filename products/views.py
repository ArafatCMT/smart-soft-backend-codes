from django.shortcuts import render
from owners.models import Owner
from products import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stocks.models import Stock
from products.models import Product, Brand, Category, Unit
from rest_framework.generics import ListAPIView
from rest_framework import filters
# Create your views here.

class CategoryView(APIView):
    serializer_class = serializers.CategorySerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=owner)
            return Response({'details': 'category added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowCategory(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.UnitSerializer
    filter_backends = [ShowCategory]

class CategoryWiseProductView(APIView):
    serializer_class = serializers.ProductSerializer

    def get(self, request, id, format=None):
        # owner = Owner.objects.get(user = request.user)
        category = Category.objects.get(id=id)
        queryset = Product.objects.all()
        products = queryset.filter(category=category)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)

    
class ProductView(APIView):
    serializer_class = serializers.ProductSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data['name']
            category =  serializer.validated_data['category']
            brand = serializer.validated_data['brand']
            unit = serializer.validated_data['unit']
            sale_price = serializer.validated_data['sale_price']
            purchase_cost = serializer.validated_data['purchase_cost']
            # serializer.save(owner=owner)
            product = Product.objects.create(owner=owner, name=name, category=category, brand=brand, unit=unit, sale_price=sale_price, purchase_cost=purchase_cost)
            product.save()
            stock = Stock.objects.create(owner=owner, product=product)
            stock.save()
            # product.delete()
            return Response({'details': 'product added successfully'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ShowProduct(filters.BaseFilterBackend):#
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset
    
class AllProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [ShowProduct]

class BrandView(APIView):
    serializer_class = serializers.BrandSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            serializer.save(owner=owner)
            return Response({'details': 'brand added successfully'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowBrand(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset
    
class AllBrandView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    filter_backends = [ShowBrand]

class BrandWiseProductView(APIView):
    serializer_class = serializers.ProductSerializer

    def get(self, request, id, format=None):
        # owner = Owner.objects.get(user = request.user)
        brand = Brand.objects.get(id=id)
        queryset = Product.objects.all()
        products = queryset.filter(brand=brand)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)

class UnitView(APIView):
    serializer_class = serializers.UnitSerializer

    def post(self, request, format=None):
        owner = Owner.objects.get(user = request.user)
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save(owner=owner)
            return Response({'details': 'unit added successfully'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowUnit(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        owner_id = request.query_params.get('owner_id')
        if owner_id:
            return queryset.filter(owner = owner_id)
        return queryset

class AllUnitView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = serializers.UnitSerializer
    filter_backends = [ShowUnit]




