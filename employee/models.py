from django.db import models
from datetime import time

# Create your models here.

class EmployeeCategory(models.Model):
    title = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
nine_oclock = time(9, 0)
seventeen_oclock = time(17, 0)
class EmployeeSchedule(models.Model):
    monday_show = models.BooleanField(default=True)
    monday_start = models.TimeField(default=nine_oclock)
    monday_end = models.TimeField(default=seventeen_oclock)
    tuesday_show = models.BooleanField(default=True)
    tuesday_start = models.TimeField(default=nine_oclock)
    tuesday_end = models.TimeField(default=seventeen_oclock)
    wednesday_show = models.BooleanField(default=True)
    wednesday_start = models.TimeField(default=nine_oclock)
    wednesday_end = models.TimeField(default=seventeen_oclock)
    thursday_show = models.BooleanField(default=True)
    thursday_start = models.TimeField(default=nine_oclock)
    thursday_end = models.TimeField(default=seventeen_oclock)
    friday_show = models.BooleanField(default=True)
    friday_start = models.TimeField(default=nine_oclock)
    friday_end = models.TimeField(default=seventeen_oclock)
    saturday_show = models.BooleanField(default=True)
    saturday_start = models.TimeField(default=nine_oclock)
    saturday_end = models.TimeField(default=seventeen_oclock)
    sunday_show = models.BooleanField(default=False)
    sunday_start = models.TimeField(default=nine_oclock)
    sunday_end = models.TimeField(default=seventeen_oclock)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
class Employee(models.Model):
    user = models.OneToOneField('auth.User', null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(EmployeeCategory, null=True, blank=True, on_delete=models.SET_NULL)
    schedule = models.ForeignKey(EmployeeSchedule, null=True, blank=True, on_delete=models.SET_NULL)
    salary = models.FloatField()
    salary_start_date = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey('store.Store', null=True, blank=True, on_delete=models.SET_NULL)
    join_date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField()
    salary_date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)