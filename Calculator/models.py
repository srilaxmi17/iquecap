from django.db import models

class SIPCalculator(models.Model):
    monthly_investment = models.DecimalField(max_digits=10, decimal_places=2)
    investment_period_years = models.IntegerField()
    returns_rate = models.DecimalField(max_digits=5, decimal_places=2)
    stepup_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"SIP Calculator - ID: {self.id}"
