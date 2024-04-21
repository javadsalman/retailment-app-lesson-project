from django.urls import path
from .views import StoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stores', StoreViewSet, basename='store')

urlpatterns = router.urls