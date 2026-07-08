from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('half_day', 'Half Day'),
        ('holiday', 'Holiday'),
    ]

    employee   = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date       = models.DateField()
    status     = models.CharField(max_length=10, choices=STATUS_CHOICES)
    check_in   = models.TimeField(null=True, blank=True)
    check_out  = models.TimeField(null=True, blank=True)
    note       = models.TextField(blank=True)

    class Meta:
        unique_together = ['employee', 'date']  # ek din ek hi record

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"


class LeaveRequest(models.Model):
    LEAVE_TYPES = [
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('annual', 'Annual Leave'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    employee    = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type  = models.CharField(max_length=10, choices=LEAVE_TYPES)
    from_date   = models.DateField()
    to_date     = models.DateField()
    reason      = models.TextField()
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_on  = models.DateTimeField(auto_now_add=True)

    @property
    def days_count(self):
        return (self.to_date - self.from_date).days + 1