from rest_framework import serializers
from ..models import EmployeeCategory, Employee

class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        exclude = ['deleted']
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    employee_category = EmployeeCategorySerializer(read_only=True)
    class Meta:
        model = Employee
        exclude = ['deleted']
