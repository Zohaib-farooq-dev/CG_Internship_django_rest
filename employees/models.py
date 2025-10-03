from django.db import models
from departments.models import Department

class Employees(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department, 
        related_name="employees", 
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.emp_name
