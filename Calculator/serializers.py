from rest_framework import serializers
from Calculator.models import SIPCalculator


class SIPCalculatorSerializer(serializers.ModelSerializer):
    future_value = serializers.SerializerMethodField()

    class Meta:
        model = SIPCalculator
        fields = ['id', 'monthly_investment', 'investment_period_years', 'returns_rate', 'stepup_percentage', 'future_value']

    def get_future_value(self, obj):
        # Example calculation
        monthly_investment = obj.monthly_investment
        investment_period_years = obj.investment_period_years
        returns_rate = obj.returns_rate / 100
        stepup_percentage = obj.stepup_percentage / 100

        future_value = 0
        for year in range(1, investment_period_years + 1):
            yearly_investment = monthly_investment * 12 * (1 + stepup_percentage) ** (year - 1)
            future_value += yearly_investment * ((1 + returns_rate) ** (investment_period_years - year + 1))

        return round(future_value, 2)