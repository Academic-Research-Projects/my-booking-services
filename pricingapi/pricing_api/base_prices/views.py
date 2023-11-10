from http import HTTPStatus
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from core.auth import Auth
from price_variations.models import PriceVariation
from price_variations.serializers import PriceVariationSerializer
from .models import BasePrice
from .serializers import BasePriceSerializer

# Create your views here.


# view to get the list of base prices and create new base price
class BasePricesView(generics.ListCreateAPIView):
    queryset = BasePrice.objects.all()
    serializer_class = BasePriceSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)

    def get(self, _):
        base_prices = BasePrice.objects.all()
        return Response([self.formatBasePrice(base_price) for base_price in base_prices])

    def formatBasePrice(self, base_price):
        price_variations = PriceVariation.objects.filter(
            base_price_id=base_price.id)  # retrieve price variations of the base price

        price_variations = [PriceVariationSerializer(
            price_variation).data for price_variation in price_variations]  # serialize price variations

        return {
            'id': base_price.id,
            'room_type_id': base_price.room_type_id,
            'value': base_price.value,
            'start_date': base_price.start_date,
            'end_date': base_price.end_date,
            'price_variations': price_variations
        }


# view to get the details of a base price, update and delete a base price
class BasePriceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasePrice.objects.all()
    serializer_class = BasePriceSerializer

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


# view to get the list of base prices of a room type
class RoomTypeBasePricesView(APIView):
    def get(self, _, pk=None):
        base_prices = BasePrice.objects.filter(room_type_id=pk)
        # we reuse the formatBasePrice method of BasePricesView to retrieve the price variations of each base price
        return Response([BasePricesView.formatBasePrice(BasePricesView, base_price) for base_price in base_prices])
