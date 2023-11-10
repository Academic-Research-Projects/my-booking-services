from rest_framework import serializers

from .models import PriceVariation


class PriceVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariation
        fields = '__all__'
