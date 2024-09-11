from django.db import models
from django.contrib.auth.models import User

# Create your models here

# Define InvestmentAccount model which represents a user's investment account


class InvestmentAccount(models.Model):
    name = models.CharField(max_length=100)  # Account name field.
    users = models.ManyToManyField(User, through='AccountUser',
                                   related_name='investment_accounts')

# AccountUser model link users to investment accounts with certain permissions


class AccountUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_account = models.ForeignKey(InvestmentAccount,
                                           on_delete=models.CASCADE)
    PERMISSION_CHOICES = [
        ('view', 'View Only'),  # Permission to view account details only
        ('full', 'Full CRUD'),  # Permission Create, Read, Update, Delete
        ('post', 'Post Only'),  # Permission to post transactions only
    ]
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

# Defines Transaction model, representing financial transactions for account


class Transaction(models.Model):
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE,
                                related_name='transactions')
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2)  # Transaction amount
    timestamp = models.DateTimeField(auto_now_add=True)  # Date of transaction
