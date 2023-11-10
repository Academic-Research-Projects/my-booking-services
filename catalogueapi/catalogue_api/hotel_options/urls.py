from django.urls import path

from .views import HotelOptionsView, HotelOptionView, HotelHotelOptionsView

urlpatterns = [
    path('', HotelOptionsView.as_view(), name='hotel-options'),
    path('<int:pk>/', HotelOptionView.as_view(), name='hotel-option'),
    path('hotel/<int:pk>/', HotelHotelOptionsView.as_view(),
         name='hotel-hotel-options'),  # url to get all hotel options for a given hotel
]
