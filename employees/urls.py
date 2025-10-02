from django.urls import path
from . import views

urlpatterns = [
    path("", views.Employee.as_view()),
    path("<str:emp_id>/", views.EmployeeDetail.as_view()),
]
