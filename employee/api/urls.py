from django.urls import path
from .views import EmployeeCategoryViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee_categories', EmployeeCategoryViewSet, basename='employee_category')
router.register('employees', EmployeeViewSet, basename='employee')

urlpatterns = router.urls