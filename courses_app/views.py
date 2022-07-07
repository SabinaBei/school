from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from courses_app.models import Course
from courses_app.serializers import CourseSerializers
from rest_framework import viewsets
from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Course
        fields = ['price']


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['name', 'duration', 'price']
    ordering_fields = ['name', 'duration', 'price']
    filterset_class = CourseFilter