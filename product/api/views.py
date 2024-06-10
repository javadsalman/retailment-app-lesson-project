from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils import timezone
from .serializers import ProductCategorySerializer, ProductSerializer, ProductItemSerializer, InvoiceSerializer, InvoiceProductSerializer
from ..models import ProductCategory, Product, ProductItem, Invoice, InvoiceProduct

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.filter(deleted=False)
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
        

class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.filter(deleted=False)
    serializer_class = ProductItemSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
        
        
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.filter(deleted=False)
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
        

class InvoiceProductViewSet(viewsets.ModelViewSet):
    queryset = InvoiceProduct.objects.filter(deleted=False)
    serializer_class = InvoiceProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()