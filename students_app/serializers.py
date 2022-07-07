from students_app.models import Student
from rest_framework import serializers


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course']
