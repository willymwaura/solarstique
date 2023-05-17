from rest_framework import serializers
from .models import CarbonCredit, CarbonCreditPurchase


class CarbonCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCredit
        fields = '__all__'


class CarbonCreditPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCreditPurchase
        fields = '__all__'
