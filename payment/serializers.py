# payment/serializers.py

from rest_framework import serializers
from appback.models import *

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'
