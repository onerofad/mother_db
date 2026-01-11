from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, MakeRequest, Support, RegisterWatcher, Chats, Cards, Notification
from .serializers import RegisterSerializer, MakeRequestSerializer, SupportSerializer, RegisterWatcherSerializer, ChatSerializer, CardSerializer, NotificationSerializer

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

class RegisterWatcherView(viewsets.ModelViewSet):
    queryset = RegisterWatcher.objects.all()
    serializer_class = RegisterWatcherSerializer

class ChatView(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class = ChatSerializer

class CardView(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer

class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer