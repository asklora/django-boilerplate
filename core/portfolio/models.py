import uuid
from django.db import IntegrityError
from django.db import models
from core.services.general import generate_id
from core.services.models import BaseTimeStampModel
from core.user.models import UserAbstract
from core.universe.models import UniverseAbstract
from core.bot.models import BotOptionTypeAbstract

class OrderAbstract(BaseTimeStampModel):
    order_uid = models.UUIDField(primary_key=True, editable=False)
    user_id = models.ForeignKey(UserAbstract, on_delete=models.CASCADE, related_name="order_user_id", db_column="user_id")
    ticker = models.ForeignKey(UniverseAbstract, on_delete=models.CASCADE, related_name="order_ticker", db_column="ticker")
    bot_id = models.ForeignKey(BotOptionTypeAbstract, on_delete=models.CASCADE, related_name="order_bot_id", db_column="bot_id")
    setup = models.JSONField(blank=True, null=True, default=dict)
    order_type = models.CharField(max_length=75, null=True, blank=True)
    placed = models.BooleanField(default=False)
    status = models.CharField(max_length=10, null=True, blank=True, default="review")
    side = models.CharField(max_length=10, default="buy")
    amount = models.FloatField(default = 0)
    placed_at = models.DateTimeField(null=True, blank=True)
    filled_at = models.DateTimeField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    order_summary = models.JSONField(blank=True, null=True, default=dict)
    is_init = models.BooleanField(default=True)
    performance_uid = models.CharField(null=True, blank=True, max_length=255)
    price = models.FloatField(null=True, blank=True)
    qty = models.FloatField(null=True, blank=True)
    exchange_rate = models.FloatField(null=True, blank=True,default=1)

    class Meta:
        abstract = True

class OrderPositionAbstract(BaseTimeStampModel):
    position_uid = models.CharField(primary_key=True, editable=False, max_length=500)
    user_id = models.ForeignKey(UserAbstract, on_delete=models.CASCADE, related_name="position_user_id", db_column="user_id")
    ticker = models.ForeignKey(UniverseAbstract, on_delete=models.CASCADE, related_name="position_ticker", db_column="ticker")
    bot_id = models.ForeignKey(BotOptionTypeAbstract, on_delete=models.CASCADE, related_name="position_bot_id", db_column="bot_id")
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
    bot_share_num = models.FloatField(null=True, blank=True,default=0)
    exchange_rate = models.FloatField(null=True, blank=True,default=1)

    class Meta:
        abstract = True

class PositionPerformance(BaseTimeStampModel):
    performance_uid = models.CharField(max_length=255, primary_key=True, editable=False)
    position_uid = models.ForeignKey(OrderPositionAbstract, on_delete=models.CASCADE, related_name="order_position", db_column="position_uid")
    order_uid = models.ForeignKey("OrderAbstract", null=True, blank=True, on_delete=models.SET_NULL, db_column="order_uid")
    last_spot_price = models.FloatField(null=True, blank=True)
    last_live_price = models.FloatField(null=True, blank=True)
    current_pnl_ret = models.FloatField(null=True, blank=True)
    current_pnl_amt = models.FloatField(null=True, blank=True)
    current_bot_cash_balance = models.FloatField(null=True, blank=True)
    share_num = models.FloatField(null=True, blank=True)
    current_investment_amount = models.FloatField(null=True, blank=True)
    last_hedge_delta = models.FloatField(null=True, blank=True)
    order_summary = models.JSONField(null=True, blank=True)
    status = models.CharField(null=True, blank=True, max_length=200)
    exchange_rate = models.FloatField(null=True, blank=True,default=1)

    class Meta:
        abstract = True