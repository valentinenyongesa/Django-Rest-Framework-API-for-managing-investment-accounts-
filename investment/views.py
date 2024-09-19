# investment/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import InvestmentAccount, Transaction, AccountUser
from .serializers import InvestmentAccountSerializer
from .serializers import TransactionSerializer
from .serializers import AccountUserSerializer
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum

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

    @action(detail=False, methods=['get'], url_path='admin-transactions',
            url_name='admin_transactions')
    def admin_transactions(self, request):
        user_id = request.query_params.get('user_id')  # Fetch user ID
        start_date = request.query_params.get('start_date')  # Fetch start date
        end_date = request.query_params.get('end_date')  # Fetch the end date

        # If user_id is missing, return an error
        if not user_id:
            return Response({'error': 'User ID is required'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Handle date parsing with default values
        try:
            start_date = datetime.strptime(start_date,
                                           '%Y-%m-%d') if start_date else timezone.now().replace(year=1900)
            end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else timezone.now()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        # Filter transactions by user and date range
        transactions = Transaction.objects.filter(
            account__users__id=user_id,
            timestamp__range=[start_date, end_date]
        )

        # Sum the transaction amounts
        total_amount = transactions.aggregate(total=Sum('amount'))['total'] or 0

        # Serialize the filtered transactions
        serializer = self.get_serializer(transactions, many=True)

        # Return the total amount and transaction details
        return Response({
            'total_amount': total_amount,
            'transactions': serializer.data
        }, status=status.HTTP_200_OK)
# ViewSet for the AccountUser model.


class AccountUserViewSet(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
