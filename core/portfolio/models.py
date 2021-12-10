from django.db import models

from django.db import models
from core.djangomodule.models import BaseTimeStampModel
from core.universe.models import Universe
from core.user.models import User
from django.db import IntegrityError
import uuid
from core.djangomodule.general import generate_id
from simple_history.models import HistoricalRecords

class Order(BaseTimeStampModel):
    order_uid = models.UUIDField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order", db_column="user_id")
    ticker = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name="symbol_order", db_column="ticker")
    bot_id = models.CharField(max_length=255, null=True, blank=True)
    setup = models.JSONField(blank=True, null=True, default=dict)
    order_type = models.CharField(max_length=75, null=True, blank=True)
    placed = models.BooleanField(default=False)
    status = models.CharField(max_length=10, null=True, blank=True, default="review")
    side = models.CharField(max_length=10, default="buy")
    amount = models.FloatField() # default
    placed_at = models.DateTimeField(null=True, blank=True)
    filled_at = models.DateTimeField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    order_summary = models.JSONField(blank=True, null=True, default=dict)
    is_init = models.BooleanField(default=True)
    price = models.FloatField()
    performance_uid = models.CharField(null=True, blank=True, max_length=255)
    qty = models.FloatField(null=True, blank=True)# disini x margin
    history = HistoricalRecords(table_name='order_changes_history')
    margin = models.FloatField(null=True, blank=True,default=1)
    exchange_rate = models.FloatField(null=True, blank=True,default=1)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if not self.order_uid:
            self.order_uid = uuid.uuid4().hex
            # using your function as above or anything else
            success = False
            failures = 0
            while not success:
                try:
                    super(Order, self).save(*args, **kwargs)
                except IntegrityError:
                    failures += 1
                    if failures > 5:
                        raise KeyError
                    else:
                        self.order_uid = uuid.uuid4().hex
                else:
                    success = True
        else:
            super().save(*args, **kwargs)


class OrderPosition(BaseTimeStampModel):
    position_uid = models.CharField(primary_key=True, editable=False, max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_position", db_column="user_id")
    ticker = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name="ticker_ordered", db_column="ticker")
    bot_id = models.CharField(max_length=255, null=True, blank=True)  # user = stock
    expiry = models.DateField(null=True, blank=True)
    spot_date = models.DateField(null=True, blank=True)
    entry_price = models.FloatField(null=True, blank=True)
    investment_amount = models.FloatField(default=0)
    max_loss_pct = models.FloatField(null=True, blank=True)
    max_loss_price = models.FloatField(null=True, blank=True)
    max_loss_amount = models.FloatField(null=True, blank=True)
    target_profit_pct = models.FloatField(null=True, blank=True)
    target_profit_price = models.FloatField(null=True, blank=True)
    target_profit_amount = models.FloatField(null=True, blank=True)
    bot_cash_balance = models.FloatField(null=True, blank=True)
    event = models.CharField(max_length=75, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    final_price = models.FloatField(null=True, blank=True)
    final_return = models.FloatField(null=True, blank=True)
    final_pnl_amount = models.FloatField(null=True, blank=True)
    current_inv_ret = models.FloatField(null=True, blank=True,default=0)
    current_inv_amt = models.FloatField(null=True, blank=True,default=0)
    is_live = models.BooleanField(default=False)
    share_num = models.FloatField(null=True, blank=True,default=0)
    vol = models.FloatField(null=True, blank=True)
    margin = models.FloatField(default=1)
    bot_cash_dividend = models.FloatField(null=True, blank=True, default=0)
    history = HistoricalRecords(table_name='order_position_history')
    exchange_rate = models.FloatField(null=True, blank=True,default=1)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.position_uid:
            self.position_uid = uuid.uuid4().hex
            success = False
            failures = 0
            while not success:
                try:
                    super(OrderPosition, self).save(*args, **kwargs)
                except IntegrityError:
                    failures += 1
                    if failures > 5:
                        raise KeyError
                    else:
                        self.position_uid = uuid.uuid4().hex
                else:
                    success = True
        else:
            super().save(*args, **kwargs)

class PositionPerformance(BaseTimeStampModel):
    performance_uid = models.CharField(max_length=255, primary_key=True, editable=False)
    position_uid = models.ForeignKey(OrderPosition, on_delete=models.CASCADE, related_name="order_position", db_column="position_uid")
    last_spot_price = models.FloatField(null=True, blank=True)
    last_live_price = models.FloatField(null=True, blank=True)
    current_pnl_ret = models.FloatField(null=True, blank=True)
    current_pnl_amt = models.FloatField(null=True, blank=True)
    current_bot_cash_balance = models.FloatField(null=True, blank=True)
    share_num = models.FloatField(null=True, blank=True)
    current_investment_amount = models.FloatField(null=True, blank=True)
    last_hedge_delta = models.FloatField(null=True, blank=True)
    option_price = models.FloatField(null=True, blank=True)
    strike = models.FloatField(blank=True, null=True)
    barrier = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)
    q = models.FloatField(blank=True, null=True)
    v1 = models.FloatField(blank=True, null=True)
    v2 = models.FloatField(blank=True, null=True)
    # delta = models.FloatField(blank=True, null=True)
    strike_2 = models.FloatField(blank=True, null=True)
    # order response from third party
    order_summary = models.JSONField(null=True, blank=True)
    order_uid = models.ForeignKey("Order", null=True, blank=True, on_delete=models.SET_NULL, db_column="order_uid")
    status = models.CharField(null=True, blank=True, max_length=200)
    exchange_rate = models.FloatField(null=True, blank=True,default=1)

    def save(self, *args, **kwargs):
        if not self.performance_uid:
            self.performance_uid = generate_id(9)
        success = False
        failures = 0
        while not success:
            try:
                super(PositionPerformance, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:
                    raise KeyError
                else:
                    self.performance_uid = generate_id(9)
            else:
                success = True

    class Meta:
        abstract = True