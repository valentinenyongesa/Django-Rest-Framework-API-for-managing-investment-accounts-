# investment/views.py
from rest_framework import viewsets, permissions
from .models import InvestmentAccount, Transaction, AccountUser
from .serializers import InvestmentAccountSerializer
from .serializers import TransactionSerializer
from .serializers import AccountUserSerializer

# ViewSet for the InvestmentAccount model.


class InvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = InvestmentAccount.objects.all()  # Fetch all investment accounts
    serializer_class = InvestmentAccountSerializer  # Use defined serializer

# ViewSet for the Transaction model.


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_permissions(self):
        # Defines custom permissions based on the requirements.
        return [permissions.IsAuthenticated()]

# ViewSet for the AccountUser model.


class AccountUserViewSet(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
