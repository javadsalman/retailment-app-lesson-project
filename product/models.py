from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    bar_code = models.CharField(max_length=200, null=True, blank=True)
    store = models.ForeignKey('store.Store', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class ProductFeature(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField()
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class ProductItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    expired_date = models.DateTimeField(null=True, blank=True)
    store = models.ForeignKey('store.Store', null=True, blank=True, on_delete=models.SET_NULL)
    custom_price = models.FloatField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
class Invoice(models.Model):
    store = models.ForeignKey('store.Store', null=True, blank=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey('employee.Employee', null=True, blank=True, on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    price = models.FloatField()
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)