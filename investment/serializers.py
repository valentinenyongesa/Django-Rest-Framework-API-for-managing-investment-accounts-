# investment/serializers.py
from rest_framework import serializers
from .models import InvestmentAccount, AccountUser, Transaction

# Serializer for the InvestmentAccount model.


class InvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentAccount
        fields = '__all__'  # Include all fields of the model.

# Serializer for the AccountUser model.


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = '__all__'

# Serializer for the Transaction model.


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
