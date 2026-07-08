from django.db import models
from employees.models import Employee

class SalarySlip(models.Model):
    employee     = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month        = models.IntegerField()
    year         = models.IntegerField()

    # Earnings
    basic        = models.DecimalField(max_digits=10, decimal_places=2)
    hra          = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allowances   = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Deductions
    pf           = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax          = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary   = models.DecimalField(max_digits=10, decimal_places=2)
    generated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['employee', 'month', 'year']

    def save(self, *args, **kwargs):
        # Auto calculate
        self.gross_salary = self.basic + self.hra + self.allowances
        self.net_salary   = self.gross_salary - self.pf - self.tax
        super().save(*args, **kwargs)