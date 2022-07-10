from school_app.models import School
from rest_framework import serializers


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'location', 'phone_number']