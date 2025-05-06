# core/models.py
from django.db import models
from django.contrib.auth.models import User

class AgriculturalData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    year = models.IntegerField()
    area_harvested_ha = models.FloatField()
    rainfall_mm = models.FloatField()
    temperature_c = models.FloatField()
    policy_flag = models.CharField(max_length=50)
    transport_cost_usd = models.FloatField()
    demand_supply_gap = models.FloatField()
    predicted_production = models.FloatField(null=True, blank=True)
    predicted_yield = models.FloatField(null=True, blank=True)
    predicted_price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.crop} in {self.country} ({self.year})"