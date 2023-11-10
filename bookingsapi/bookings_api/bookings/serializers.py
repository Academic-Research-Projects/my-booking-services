from rest_framework import serializers
from bookings.models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        #fields = ['id', 'start_date', 'end_date', 'love_pack', 'breakfast', room_id, user_id]
        fields = '__all__'
