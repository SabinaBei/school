from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from students_app.models import Student
from students_app.serializers import StudentSerializers
from rest_framework import viewsets

class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']