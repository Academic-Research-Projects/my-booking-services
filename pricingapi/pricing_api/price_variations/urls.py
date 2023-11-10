from django.urls import path
from .views import PriceVariationView, PriceVariationsView, BasePricePriceVariationsView


urlpatterns = [
    path('', PriceVariationsView.as_view(), name='price-variations'),
    path('<int:pk>/', PriceVariationView.as_view(), name='price-variation'),
    path('base-price/<int:pk>/', BasePricePriceVariationsView.as_view(),
         name='price-variation-base-price'),  # url to get the list of price variations of a base price
]
