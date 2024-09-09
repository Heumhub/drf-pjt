from django.shortcuts import render
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class Profile(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field='username'
    permission_classes = [IsAuthenticated]