from http import HTTPStatus
from rest_framework.response import Response
import requests
from rest_framework import generics
from rest_framework.views import APIView

from .models import RoomType
from .serializers import RoomTypeSerializer
from core.auth import Auth


# I didn't find a way to keep using generics.ListCreateAPIView while calling another api
class RoomTypesView(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    # this line is still useful for post method convenience in the browser
    serializer_class = RoomTypeSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)

    def get(self, request):
        room_types = RoomType.objects.all()
        return Response([self.formatRoomType(room_type) for room_type in room_types], status=HTTPStatus.OK)

    # there is certainly a better way to do this (we call the pricing api for each room type)
    # but I would say our goal is to provide a working api quickly
    def formatRoomType(self, room_type):
        try:
            base_prices = requests.get(
                f'http://localhost:8003/base-prices/room-type/{room_type.id}').json()  # call pricing api TODO use env variable
            return {
                'id': room_type.id,
                'name': room_type.name,
                'capacity': room_type.capacity,
                'base_prices': base_prices
            }
        except Exception:  # in case the pricing api is not reachable
            return {
                'id': room_type.id,
                'name': room_type.name,
                'capacity': room_type.capacity,
                'base_prices': []
            }


class RoomTypeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

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
            result.status_code = Auth.getUser(request)

            if result != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().delete(request, *args, **kwargs)
