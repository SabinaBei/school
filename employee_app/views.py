from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from employee_app.models import Employee, Position, Department
from employee_app.serializers import EmployeeSerializers, PositionSerializers, DepartmentSerializers
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']


class PositionViewSet(viewsets.ModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Position.objects.all().order_by('-id')
    serializer_class = PositionSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class DepartmentViewSet(viewsets.ModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Department.objects.all().order_by('-id')
    serializer_class = DepartmentSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


# QuerySet — это набор данных из базы данных.
# QuerySet создается как список объектов.
# QuerySets упрощает получение данных, которые вам действительно нужны, позволяя фильтровать и упорядочивать данные.