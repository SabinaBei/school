from employee_app.models import Employee, Position, Department
from rest_framework import serializers
from auth_app.serializers import UserSerializer


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course', 'position', 'salary']
        fields = ['user', 'date_of_birth', 'phone_number', 'gender', 'course', 'position', 'salary']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        serializers_user = UserSerializer(instance=instance.user)
        response["user"] = serializers_user.data
        return response


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'duration', 'description']


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'description']