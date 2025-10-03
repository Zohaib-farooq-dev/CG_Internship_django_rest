from rest_framework import serializers
from employees.models import Employees
from departments.serializers import DepartmentSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)   # Nested representation
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Employees.objects.all(),
        source="department",
        write_only=True
    )

    class Meta:
        model = Employees
        fields = ['emp_id', 'emp_name', 'designation', 'department', 'department_id']