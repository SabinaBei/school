from courses_app.models import Course
from rest_framework import serializers


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']
