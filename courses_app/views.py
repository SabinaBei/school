from courses_app.models import Course
from courses_app.serializers import CourseSerializers
from rest_framework import viewsets


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

