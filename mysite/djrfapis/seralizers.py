from rest_framework import serializers
from .models import Student


# studentSerializer for serializing student data
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'name', 'age', 'description'
        )
