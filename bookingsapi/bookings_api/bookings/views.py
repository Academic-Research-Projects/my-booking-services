# from requests import request
import requests
from bookings.models import Bookings
from bookings.serializers import BookingsSerializer  # , UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from http import HTTPStatus

from core.auth import Auth


class BookingsList(generics.ListCreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

    def post(self, request):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().post(request)

    def get(self, request, *args, **kwargs):
        bookings = Bookings.objects.all()
        return super().get(request, *args, **kwargs)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

    def get(self, request, *args, **kwargs):
        try:
            result = Auth.getUser(request)

            if result.status_code != 200:
                return Response({'error': 'unauthorized'}, status=HTTPStatus.UNAUTHORIZED)

        except Exception:
            return Response({'error': 'users api is not reachable'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return super().get(request, *args, **kwargs)

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

# views de test en monolithique
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

################ tutorial 3 official django rest framework page#####################
# from bookings.models import Bookings
# from bookings.serializers import BookingsSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class BookingsList(APIView):
#     """
#     List all bookings, or create a new booking.
#     """
#     def get(self, request, format=None):
#         bookings = Bookings.objects.all()
#         serializer = BookingsSerializer(bookings, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookingsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookingDetail(APIView):
#     """
#     Retrieve, update or delete a booking instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Bookings.objects.get(pk=pk)
#         except Bookings.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         booking = self.get_object(pk)
#         serializer = BookingsSerializer(booking)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         booking = self.get_object(pk)
#         serializer = BookingsSerializer(booking, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         booking = self.get_object(pk)
#         booking.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


############### tutorial 1 django official page#####################

# @csrf_exempt
# def bookings_list(request):
#     """
#     List all bookings, or create a new booking.
#     """
#     if request.method == 'GET':
#         bookings = Bookings.objects.all()
#         serializer = BookingsSerializer(bookings, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BookingsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def booking_detail(request, pk):
#     """
#     Retrieve, update or delete a booking.
#     """
#     try:
#         booking = Bookings.objects.get(pk=pk)
#     except Bookings.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = BookingsSerializer(booking)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BookingsSerializer(booking, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         booking.delete()
#         return HttpResponse(status=204)
