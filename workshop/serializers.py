from rest_framework import serializers
from .models import Bagan

class BaganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bagan
        fields = '__all__'