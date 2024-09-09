from django.shortcuts import render
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer
from rest_framework import generics
# Create your views here.
class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer()