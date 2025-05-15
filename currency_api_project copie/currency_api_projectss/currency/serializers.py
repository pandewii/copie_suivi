from rest_framework import serializers
from .models import TNDconv, DZDconv

class TNDconvSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNDconv
        fields = '__all__'

class DZDconvSerializer(serializers.ModelSerializer):
    class Meta:
        model = DZDconv
        fields = '__all__'