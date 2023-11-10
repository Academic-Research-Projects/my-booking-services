from http import HTTPStatus
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from core.auth import Auth

from .serializers import HotelOptionPriceSerializer
from .models import HotelOptionPrice

# Create your views here.


class HotelOptionPricesView(generics.ListCreateAPIView):
    queryset = HotelOptionPrice.objects.all()
    serializer_class = HotelOptionPriceSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)


class HotelOptionPriceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotelOptionPrice.objects.all()
    serializer_class = HotelOptionPriceSerializer

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


class HotelOptionHotelOptionPricesView(APIView):
    def get(self, _, pk=None):
        hotel_option_prices = HotelOptionPrice.objects.filter(
            hotel_option_id=pk)
        serializer = HotelOptionPriceSerializer(hotel_option_prices, many=True)
        return Response(serializer.data)
