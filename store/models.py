from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=200)
    customer = models.ForeignKey('customer.Customer', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=True)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)