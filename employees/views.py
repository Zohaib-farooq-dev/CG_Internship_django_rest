from django.shortcuts import render
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