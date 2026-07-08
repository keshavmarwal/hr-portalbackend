from rest_framework import serializers
from .models import JobPosting, Candidate

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    
    class Meta:
        model = Candidate
        fields = '__all__'
