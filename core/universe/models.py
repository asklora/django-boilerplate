from django.db import models

class CurrencyAbstract(models.Model):
    currency_code = models.CharField(primary_key=True, max_length=30)
    currency_name = models.CharField(blank=True, null=True, max_length=255)
    is_decimal = models.BooleanField(default=False)
    last_price = models.FloatField(blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

class UniverseAbstract(models.Model):
    ticker = models.CharField(max_length=255, primary_key=True)
    created = models.DateField(blank=True, null=True)
    updated = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    ticker_name = models.TextField(blank=True, null=True)


    class Meta:
        abstract = True