from django.urls import path
from .views import DepartmentListCreate, DepartmentDetail

urlpatterns = [
    path('', DepartmentListCreate.as_view()),
    path('<int:pk>/', DepartmentDetail.as_view()),
]
