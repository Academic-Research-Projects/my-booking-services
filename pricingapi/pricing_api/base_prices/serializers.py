from rest_framework import serializers

from .models import BasePrice


class BasePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePrice
        fields = '__all__'
