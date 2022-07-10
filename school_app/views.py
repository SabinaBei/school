from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from school_app.models import School
from school_app.serializers import SchoolSerializers
from rest_framework import viewsets


class SchoolViewSet(viewsets.ModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = School.objects.all()
    serializer_class = SchoolSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
