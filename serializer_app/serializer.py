__author__ = 'USER'
from rest_framework import serializers
from serializer_app.models import questions
class questionsserializer(serializers.ModelSerializer):
    class Meta:
        model=questions
        fields=[
            'title',
            'status',
            'created_by'
        ]
