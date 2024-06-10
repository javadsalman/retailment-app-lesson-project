from rest_framework import serializers
from ..models import Product, ProductCategory, ProductItem, Invoice, InvoiceProduct


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        exclude = ('deleted', 'updated')
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('deleted', 'updated')
        
        
class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        exclude = ('deleted', 'updated')
        
        
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        exclude = ('deleted', 'updated')
        
        
class InvoiceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceProduct
        exclude = ('deleted', 'updated')