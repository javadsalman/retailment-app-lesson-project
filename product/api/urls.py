from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductCategoryViewSet, ProductViewSet, ProductItemViewSet, InvoiceViewSet, InvoiceProductViewSet

router = DefaultRouter()
router.register('product_categories', ProductCategoryViewSet, basename='product_categories')
router.register('products', ProductViewSet, basename='products')
router.register('product_items', ProductItemViewSet, basename='product_items')
router.register('invoices', InvoiceViewSet, basename='invoices')
router.register('invoice_products', InvoiceProductViewSet, basename='invoice_products')

urlpatterns = router.urls