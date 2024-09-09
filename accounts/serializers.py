from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['user_name', 'email', 'password', 'name', 'nickname', 'birthday', 'gender','introduction']



