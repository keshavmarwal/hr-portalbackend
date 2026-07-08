from rest_framework import serializers
from .models import Department , Employee

class DepartmentSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Department
          fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
     department_name = serializers.CharField(source = 'department.name' , read_only=True)
     full_name = serializers.ReadOnlyField() 

     class Meta:
          model = Employee
          fields = '__all__'

