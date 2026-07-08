from django.db import models

# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length=101)

    def __str__(self):
        return self.name
    

class Employee(models.Model):

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]

     # Personal Info
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    email        = models.EmailField(unique=True)
    phone        = models.CharField(max_length=15)
    gender       = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    photo        = models.ImageField(upload_to='employees/', null=True, blank=True)

    # Job Info
    employee_id  = models.CharField(max_length=20, unique=True)
    department   = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation  = models.CharField(max_length=100)
    date_joined  = models.DateField()
    salary       = models.DecimalField(max_digits=10, decimal_places=2)
    status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_id} -> {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"