from employee_app.models import Employee
from rest_framework import serializers


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course']