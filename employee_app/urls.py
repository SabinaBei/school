from django.urls import path
from employee_app.views import EmployeeViewSet

urlpatterns = [
    path('', EmployeeViewSet.as_view({'get': 'list'}), name='employee-list')
    ]