from rest_framework import serializers

from .models import HotelOptionPrice


class HotelOptionPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelOptionPrice
        fields = '__all__'
