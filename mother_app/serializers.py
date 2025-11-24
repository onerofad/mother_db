from rest_framework import serializers
from .models import Register, MakeRequest, Support, RegisterWatcher, Chats

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class MakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MakeRequest

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Support

class RegisterWatcherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RegisterWatcher

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Chats