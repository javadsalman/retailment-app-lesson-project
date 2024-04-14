from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscription(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    duration = models.IntegerField()
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

GENDER_CHOICES = (
    ('male', 'Male',),
    ('female', 'Female',),
    ('other', 'Other',),
)
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL)
    subscribtion_date = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    def __str__(self):
        return self.user.username # type: ignore
    
class Payment(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField()
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.customer.user.username} - {self.subscription.title}' # type: ignore
