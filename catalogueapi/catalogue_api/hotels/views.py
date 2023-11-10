from http import HTTPStatus
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from hotel_options.serializers import HotelOptionSerializer
from hotel_options.models import HotelOption

from .serializers import HotelSerializer
from .models import Hotel
from core.auth import Auth

# Create your views here.


# view to get the list of hotels and create new hotel
class HotelsView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)

    def get(self, _):
        hotels = Hotel.objects.all()
        return Response([self.formatHotel(hotel) for hotel in hotels])

    def formatHotel(self, hotel):
        hotel_options = HotelOption.objects.filter(hotel_id=hotel.id)

        hotel_options = [HotelOptionSerializer(
            hotel_option).data for hotel_option in hotel_options]  # serialize hotel_options

        return {
            'id': hotel.id,
            'name': hotel.name,
            'address': hotel.address,
            'phone': hotel.phone,
            'hotel_options': hotel_options
        }


# view to get a single hotel, update and delete
class HotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def put(self, request, *args, **kwargs):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().delete(request, *args, **kwargs)
