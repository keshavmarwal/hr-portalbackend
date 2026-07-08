from rest_framework import viewsets
from .models import SalarySlip
from .serializers import SalarySlipSerializer

class SalarySlipViewSet(viewsets.ModelViewSet):
    queryset = SalarySlip.objects.all().select_related('employee')
    serializer_class = SalarySlipSerializer
