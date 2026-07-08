from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().select_related('department')
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'employee_id']
    ordering_fields = ['date_joined', 'first_name']

    # Active employees only
    @action(detail=False, methods=['get'])
    def active(self, request):
        active_emps = Employee.objects.filter(status='active')
        serializer = self.get_serializer(active_emps, many=True)
        return Response(serializer.data)