from django.shortcuts import get_object_or_404, render
from . models import Employees
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status

class Employee(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
     def get(self, request, emp_id):
        employee = get_object_or_404(Employees, emp_id=emp_id) 
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
        