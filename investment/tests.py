# investment/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import InvestmentAccount, AccountUser, Transaction
from django.contrib.auth.models import User

# Tests for InvestmentAccount APIs.
class InvestmentAccountTests(APITestCase):

    def setUp(self):
        # Setup test data, such as creating a test user.
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_investment_account(self):
        # Example of testing the creation of an investment account.
        self.client.login(username='testuser', password='testpass')  # Log in the test user.
        url = reverse('investmentaccount-list')  # Get the URL for the list view.
        data = {'name': 'New Investment Account'}  # Define data to post.
        response = self.client.post(url, data, format='json')  # Make a POST request.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check the response.
