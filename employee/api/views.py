from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils import timezone
from .serializers import EmployeeCategorySerializer, EmployeeSerializer
from ..models import EmployeeCategory, Employee

class EmployeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCategory.objects.filter(deleted=False)
    serializer_class = EmployeeCategorySerializer
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(deleted=False)
    serializer_class = EmployeeSerializer
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
