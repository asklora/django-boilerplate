import uuid
import base64
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class BaseTimeStampModel(models.Model):
    """
    Base model for timestamp support, related models: :model:`Clients.Client` and its related models, :model:`orders.Order` etc.
    """
    created = models.DateTimeField(editable=True)
    updated = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(BaseTimeStampModel, self).save(*args, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    WAIT, APPROVED ,UNVERIFIED,VERIFIED= "in waiting list", "approved","unverified","verified"
    status_choices = (
        (UNVERIFIED, "unverified"),
        (VERIFIED, "verified"),
        (WAIT, "in waiting list"),
        (APPROVED, "approved"),
    )
    email = models.EmailField(("email address"),null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "username"
    AUTH_FIELD_NAME = "email"

    class Meta:
        abstract = True

class Accountbalance(BaseTimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_balance", db_column="user_id", primary_key=True)
    amount = models.FloatField(default=0,validators=[MinValueValidator(0)])
    currency_code = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="user_currency", default="USD", db_column="currency_code")

    class Meta:
        abstract = True

class TransactionHistory(BaseTimeStampModel):
    C = "credit"
    D = "debit"
    type_choice = ((C, "credit"), (D, "debit"))
    balance_uid = models.ForeignKey(Accountbalance, on_delete=models.CASCADE, related_name="account_transaction", db_column="balance_uid")
    side = models.CharField(max_length=100, choices=type_choice)
    amount = models.FloatField(default=0)
    transaction_detail = models.JSONField(default=dict, null=True, blank=True)
    
    class Meta:
        abstract = True