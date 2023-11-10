from django.urls import path

from .views import BasePriceView, BasePricesView, RoomTypeBasePricesView

urlpatterns = [
    path('', BasePricesView.as_view(), name='base-prices'),
    path('<int:pk>/', BasePriceView.as_view(), name='base-price'),
    path('room-type/<int:pk>/', RoomTypeBasePricesView.as_view(),
         name='base-price-room-type'),  # url to get the list of base prices of a room type
]
