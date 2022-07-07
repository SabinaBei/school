from students_app.models import Student
from students_app.serializers import StudentSerializers
from rest_framework import viewsets


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
