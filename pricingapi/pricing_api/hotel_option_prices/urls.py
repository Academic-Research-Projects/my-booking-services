from django.urls import path
from .views import HotelOptionPricesView, HotelOptionPriceView, HotelOptionHotelOptionPricesView


urlpatterns = [
    path('', HotelOptionPricesView.as_view(), name='hotel-option-prices'),
    path('<int:pk>/', HotelOptionPriceView.as_view(), name='hotel-option-price'),
    path('hotel-option/<int:pk>/', HotelOptionHotelOptionPricesView.as_view(),
         name='hotel-option-price-hotel-option'),  # url to get the list of hotel option prices of a given hotel option
]
