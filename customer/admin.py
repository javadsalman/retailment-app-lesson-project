from django.contrib import admin
from .models import Subscription, Customer, Payment
# Register your models here.

admin.site.register(Subscription)
admin.site.register(Customer)
admin.site.register(Payment)