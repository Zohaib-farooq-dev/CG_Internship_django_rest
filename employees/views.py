from django.shortcuts import get_object_or_404, render
from . models import Employees
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework import generics,mixins

# class Employee(APIView):
#     def get(self, request):
#         employees = Employees.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK) 
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):
#      def get(self, request, emp_id):
#         employee = get_object_or_404(Employees, emp_id=emp_id) 
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#      def put(self, request, emp_id):
#         employee = get_object_or_404(Employees, emp_id=emp_id) 
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
#      def delete(self, request, emp_id):
#         employee = get_object_or_404(Employees, emp_id=emp_id) 
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
# Mixins
class EmployeeList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)



class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'emp_id'

    def get(self, request, emp_id):
        return self.retrieve(request, emp_id)
    
    def put(self, request, emp_id):
        return self.update(request, emp_id)
    
    def delete(self, request, emp_id):
        return self.destroy(request, emp_id)
"""


# Generics
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'emp_id'
