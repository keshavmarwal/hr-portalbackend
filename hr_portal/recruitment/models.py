from django.db import models

class JobPosting(models.Model):
    title        = models.CharField(max_length=100)
    department   = models.CharField(max_length=100)
    description  = models.TextField()
    vacancies    = models.IntegerField(default=1)
    last_date    = models.DateField()
    is_active    = models.BooleanField(default=True)
    posted_on    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('interviewed', 'Interviewed'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]

    job          = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=15)
    resume       = models.FileField(upload_to='resumes/')
    status       = models.CharField(max_length=15, choices=STATUS_CHOICES, default='applied')
    applied_on   = models.DateTimeField(auto_now_add=True)
    interview_date = models.DateField(null=True, blank=True)
    notes        = models.TextField(blank=True)