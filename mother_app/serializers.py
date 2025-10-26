from rest_framework import serializers
from .models import Register, MakeRequest

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class MakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MakeRequest