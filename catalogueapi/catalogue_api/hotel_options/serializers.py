from rest_framework import serializers

from .models import HotelOption


class HotelOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelOption
        fields = '__all__'
