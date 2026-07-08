from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Attendance, LeaveRequest
from .serializers import AttendanceSerializer, LeaveRequestSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().select_related('employee')
    serializer_class = AttendanceSerializer

    # Monthly report: /api/attendance/report/?employee=1&month=6&year=2025
    @action(detail=False, methods=['get'])
    def report(self, request):
        emp_id = request.query_params.get('employee')
        month  = request.query_params.get('month')
        year   = request.query_params.get('year')

        qs = self.queryset.filter(
            employee_id=emp_id,
            date__month=month,
            date__year=year
        )
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all().select_related('employee')
    serializer_class = LeaveRequestSerializer

    # HR approve/reject kare: POST /api/attendance/leaves/5/update_status/
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        leave = self.get_object()
        new_status = request.data.get('status')
        if new_status in ['approved', 'rejected']:
            leave.status = new_status
            leave.save()
            return Response({'message': f'Leave {new_status}'})
        return Response({'error': 'Invalid status'}, status=400)