from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, MakeRequest
from .serializers import RegisterSerializer, MakeRequestSerializer

# Create your views here.
class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class MakeRequestView(viewsets.ModelViewSet):
    queryset = MakeRequest.objects.all()
    serializer_class = MakeRequestSerializer