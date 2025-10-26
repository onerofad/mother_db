from django.shortcuts import render
from rest_framework import viewsets
from .models import Register
from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer