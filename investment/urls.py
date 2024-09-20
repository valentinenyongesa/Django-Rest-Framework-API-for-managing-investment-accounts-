# investment/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentAccountViewSet
from .views import TransactionViewSet
from .views import AccountUserViewSet

# Sets up a DefaultRouter and registers the ViewSets with it.
router = DefaultRouter()
router.register(r'investment-accounts',
                InvestmentAccountViewSet, basename='investmentaccount')  # Route for investment accounts
router.register(r'transactions', TransactionViewSet, basename='transaction')  # Route for transactions
router.register(r'account-users',
                AccountUserViewSet, basename='accountuser')  # Route for account-user relations

# Includes the router's URLs in the app's URL patterns.
urlpatterns = [
    path('', include(router.urls)),
]
