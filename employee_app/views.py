from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from employee_app.models import Employee
from employee_app.serializers import EmployeeSerializers
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
