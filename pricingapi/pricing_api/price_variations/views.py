from http import HTTPStatus
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from core.auth import Auth

from .models import PriceVariation
from .serializers import PriceVariationSerializer


# Create your views here.


class PriceVariationsView(generics.ListCreateAPIView):
    queryset = PriceVariation.objects.all()
    serializer_class = PriceVariationSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)


class PriceVariationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceVariation.objects.all()
    serializer_class = PriceVariationSerializer

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


# view to get the list of price variations of a base price
class BasePricePriceVariationsView(APIView):
    def get(self, _, pk=None):
        price_variations = PriceVariation.objects.filter(base_price_id=pk)
        serializer = PriceVariationSerializer(price_variations, many=True)
        return Response(serializer.data)
