from employee_app.models import Employee, Position, Department
from rest_framework import serializers


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course', 'position', 'salary']


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'duration', 'description', 'permission']


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'description']