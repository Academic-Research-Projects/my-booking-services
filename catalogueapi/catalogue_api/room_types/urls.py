from django.urls import path

from .views import RoomTypeView, RoomTypesView

urlpatterns = [
    path('', RoomTypesView.as_view(), name='room-types'),
    path('<int:pk>/', RoomTypeView.as_view(), name='room-type'),
]
