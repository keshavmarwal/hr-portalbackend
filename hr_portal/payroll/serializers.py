from rest_framework import serializers
from .models import SalarySlip

class SalarySlipSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    
    class Meta:
        model = SalarySlip
        fields = '__all__'
