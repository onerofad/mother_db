from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, MakeRequest, Support
from .serializers import RegisterSerializer, MakeRequestSerializer, SupportSerializer

# Create your views here.
class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class MakeRequestView(viewsets.ModelViewSet):
    queryset = MakeRequest.objects.all()
    serializer_class = MakeRequestSerializer

class SupportView(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer