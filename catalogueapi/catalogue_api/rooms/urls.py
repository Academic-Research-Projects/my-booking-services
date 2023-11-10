from django.urls import path

from .views import RoomsView, RoomView

urlpatterns = [
    # url to get the list of rooms and create new room
    # name parameter is used in reverse() in tests.py
    path('', RoomsView.as_view(), name='rooms'),

    # url to get a single room, update and delete
    path('<int:pk>/', RoomView.as_view(), name='room'),

    # keeping this code for reference of how to communicate between microservices
    # url to get the list of rooms of an hotel
    # path('hotel/<int:pk>/', HotelRoomsView.as_view(), name='hotel_rooms'),
]
