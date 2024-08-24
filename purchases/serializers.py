from rest_framework import serializers
from purchases import models
from products.models import Product
from stocks.models import Stock

class PurchaseSerializer(serializers.ModelSerializer):
    quentity = serializers.IntegerField(required = True)
    payable = serializers.IntegerField(required = True)
    class Meta:
        model = models.Purchase
        fields = ['owner', 'supplier', 'product', 'quentity', 'purchase_date', 'payable', 'paid', 'due']
        read_only_fields = ['owner', 'due']
    
    def save(self, owner):
        supplier = self.validated_data['supplier']
        product = self.validated_data['product']
        quentity = self.validated_data['quentity']
        payable = self.validated_data['payable']
        paid = self.validated_data['paid']
        due = 0

        if paid < 0:
            raise serializers.ValidationError({'error': "Invalid amount"})
        
        if paid > payable:
                due -= (paid - payable)
        if payable > paid:
                due += (payable - paid)
        
        purchase = models.Purchase.objects.create(owner=owner, supplier=supplier, product=product, payable=payable, paid=paid, due=due, quentity=quentity)
        purchase.save()
        return purchase

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale
        fields = ['owner', 'customer', 'product', 'quentity', 'date', 'receivable', 'paid', 'due', 'purchase_cost',  'profit', 'status']
        read_only_fields = ['owner', 'due', 'purchase_cost', 'profit', 'status']
    

    def save(self, owner):
        customer = self.validated_data['customer']
        product = self.validated_data['product']
        quentity = self.validated_data['quentity']
        receivable = self.validated_data['receivable']
        paid = self.validated_data['paid']
        due = 0
        status = "Unpaid"
        stock = Stock.objects.get(product=product)

        if quentity > stock.available_stock:
            raise serializers.ValidationError({'error': "Not Available on stock"})

        if paid < 0:
            raise serializers.ValidationError({'error': "Invalid amount"})
        
        if paid >= receivable:
                due -= (paid - receivable)
                status = "Paid"
        if receivable > paid:
                due += (receivable - paid)

        prod = Product.objects.get(id=product.id)
        purchase_cost = prod.purchase_cost
        profit = (prod.sale_price * quentity) - (purchase_cost * quentity)
        
        sale = models.Sale.objects.create(owner=owner, customer=customer, product=product, receivable=receivable, paid=paid, due=due, quentity=quentity, purchase_cost=purchase_cost, profit=profit, status=status)
        sale.save()
        return sale

