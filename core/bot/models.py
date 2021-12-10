from django.db import models

class BotType(models.Model):
    bot_type = models.TextField(primary_key=True)
    bot_name = models.TextField(blank=True, null=True)
    class Meta:
        abstract = True

class BotOptionType(models.Model):
    bot_id = models.TextField(primary_key=True)
    bot_type = models.ForeignKey(BotType, on_delete=models.CASCADE, db_column="bot_type", related_name="bot_option_type_bot_type", null=True)
    bot_option_type = models.TextField(blank=True, null=True)
    bot_option_name = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        
    def is_uno(self):
        return self.bot_type.bot_type == 'UNO'
    
    def is_classic(self):
        return self.bot_type.bot_type == 'CLASSIC'
    
    def is_ucdc(self):
        return self.bot_type.bot_type == 'UCDC'
    
    def is_stock(self):
        return self.bot_type.bot_type == 'STOCK'