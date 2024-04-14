from django.urls import path
from .views import SubscriptionViewSet, CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register('customers', CustomerViewSet, basename='customers')

urlpatterns = router.urls