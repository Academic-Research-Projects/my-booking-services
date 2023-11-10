from django.urls import path

from .views import HotelsView, HotelView

urlpatterns = [
    # url to get the list of hotels and create new hotel
    # name parameter is used in reverse() in tests.py
    path('', HotelsView.as_view(), name='hotels'),
    # url to get a single hotel, update and delete
    path('<int:pk>/', HotelView.as_view(), name='hotel'),
]
