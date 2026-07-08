from rest_framework import viewsets, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import JobPosting, Candidate
from .serializers import JobPostingSerializer, CandidateSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all().select_related('job')
    serializer_class = CandidateSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        candidate = self.get_object()
        new_status = request.data.get('status')
        valid = ['applied','shortlisted','interviewed','selected','rejected']
        if new_status in valid:
            candidate.status = new_status
            candidate.save()
            return Response({'message': f'Status updated to {new_status}'})
        return Response({'error': 'Invalid status'}, status=400)