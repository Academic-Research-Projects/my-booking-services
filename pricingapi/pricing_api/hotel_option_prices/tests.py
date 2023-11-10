from http import HTTPStatus
import json
from django.test import Client, TestCase
from django.urls import reverse

from .serializers import HotelOptionPriceSerializer
from .models import HotelOptionPrice

# Create your tests here.


class TestHotelOptionPrices(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('hotel-option-prices')

    def test_list_hotel_option_prices(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_hotel_option_price(self):
        data = {
            'hotel_option_id': 1,
            'value': 25,
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, HTTPStatus.CREATED)


class TestHotelOptionPrice(TestCase):
    def setUp(self):
        self.client = Client()
        self.hotel_option_price = HotelOptionPrice.objects.create(
            hotel_option_id=1, value=25, start_date='2023-01-01', end_date='2023-12-31')
        self.url = reverse('hotel-option-price',
                           args=[self.hotel_option_price.pk])

    def test_get_hotel_option_price_by_id(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = HotelOptionPriceSerializer(self.hotel_option_price)

        self.assertEqual(response.data, serializer.data)

    def test_update_hotel_option_price(self):
        data = {
            'hotel_option_id': 1,
            'value': 30,
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertEqual(HotelOptionPrice.objects.get().value, 30)

    def test_delete_hotel_option_price(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        self.assertEqual(HotelOptionPrice.objects.count(), 0)


class TestHotelOptionHotelOptionPrices(TestCase):
    def setUp(self):
        self.client = Client()
        self.hotel_option_price = HotelOptionPrice.objects.create(
            hotel_option_id=1, value=25, start_date='2023-01-01', end_date='2023-12-31')
        self.url = reverse('hotel-option-price-hotel-option',
                           args=[self.hotel_option_price.hotel_option_id])

    def test_list_hotel_option_prices_of_hotel_option(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = HotelOptionPriceSerializer(self.hotel_option_price)

        self.assertEqual(response.data[0], serializer.data)
