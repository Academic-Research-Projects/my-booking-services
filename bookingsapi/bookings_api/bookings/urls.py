from django.urls import path
from bookings import views


urlpatterns = [
    path('', views.BookingsList.as_view(), name='bookings'),
    path('<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
    # path('bookings/', views.BookingsList.as_view()),
    # path('bookings/<int:pk>/', views.BookingDetail.as_view()),
]
