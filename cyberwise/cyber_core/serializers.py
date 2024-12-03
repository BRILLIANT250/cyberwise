from rest_framework import serializers
from .models import CybersecurityContent

class CybersecurityContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CybersecurityContent
        fields = '__all__'
