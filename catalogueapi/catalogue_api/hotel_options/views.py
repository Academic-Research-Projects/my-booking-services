import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from http import HTTPStatus

from core.auth import Auth

from .models import HotelOption
from .serializers import HotelOptionSerializer

# Create your views here.


class HotelOptionsView(generics.ListCreateAPIView):
    queryset = HotelOption.objects.all()
    serializer_class = HotelOptionSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)

    def get(self, _):
        hotel_options = HotelOption.objects.all()
        return Response([self.formatHotelOption(hotel_option) for hotel_option in hotel_options])

    def formatHotelOption(self, hotel_option):
        try:
            hotel_option_prices = requests.get(
                f'http://localhost:8003/hotel-option-prices/hotel-option/{hotel_option.id}/').json()

            return {
                'id': hotel_option.id,
                'number': hotel_option.number,
                'option_type': hotel_option.option_type,
                'option_prices': hotel_option_prices,
            }
        except Exception:  # in case the pricing api is not reachable
            return {
                'id': hotel_option.id,
                'number': hotel_option.number,
                'option_type': hotel_option.option_type,
                'option_prices': [],
            }


class HotelOptionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotelOption.objects.all()
    serializer_class = HotelOptionSerializer

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


# view to get the list of hotel options of a hotel
class HotelHotelOptionsView(APIView):
    def get(self, _, pk=None):
        hotel_options = HotelOption.objects.filter(hotel_id=pk)
        # we reuse the formatHotelOption method of HotelOptionsView to retrieve the hotel option prices of each hotel option
        return Response([HotelOptionsView.formatHotelOption(HotelOptionsView, hotel_option) for hotel_option in hotel_options])
