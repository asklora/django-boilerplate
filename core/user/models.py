from core.services.models import BaseTimeStampModel
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.universe.models import CurrencyAbstract

class UserAbstract(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email address"),null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class AccountbalanceAbstract(BaseTimeStampModel):
    user = models.OneToOneField(UserAbstract, on_delete=models.CASCADE, related_name="user_balance", db_column="user_id", primary_key=True)
    amount = models.FloatField(default=0,validators=[MinValueValidator(0)])
    currency_code = models.ForeignKey(CurrencyAbstract, on_delete=models.CASCADE, related_name="user_currency", default="USD", db_column="currency_code")

    class Meta:
        abstract = True

class TransactionHistoryAbstract(BaseTimeStampModel):
    C = "credit"
    D = "debit"
    type_choice = ((C, "credit"), (D, "debit"))
    balance_uid = models.ForeignKey(AccountbalanceAbstract, on_delete=models.CASCADE, related_name="account_transaction", db_column="balance_uid")
    side = models.CharField(max_length=100, choices=type_choice)
    amount = models.FloatField(default=0)
    transaction_detail = models.JSONField(default=dict, null=True, blank=True)
    
    class Meta:
        abstract = True