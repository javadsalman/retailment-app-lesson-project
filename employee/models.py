from django.db import models
from datetime import time
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class EmployeeCategory(models.Model):
    title = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Employee(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    category = models.ForeignKey(EmployeeCategory, null=True, blank=True, on_delete=models.SET_NULL)
    salary = models.FloatField()
    salary_day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    store = models.ForeignKey('store.Store', null=True, blank=True, on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)