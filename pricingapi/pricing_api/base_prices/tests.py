from http import HTTPStatus
from django.test import Client, TestCase
from django.urls import reverse
import json

from .serializers import BasePriceSerializer
from .models import BasePrice

# Create your tests here.


class TestBasePrices(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.url = reverse('base-prices')

    def test_list_base_prices(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_base_price(self):
        data = {
            'room_type_id': 1,
            'value': 100.00,
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, HTTPStatus.CREATED)


class TestBasePrice(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.base_price = BasePrice.objects.create(
            room_type_id=1, value=100, start_date='2023-01-01', end_date='2023-12-31')
        self.url = reverse('base-price', args=[self.base_price.pk])

    def test_get_base_price_by_id(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = BasePriceSerializer(self.base_price)

        self.assertEqual(response.data, serializer.data)

    def test_update_base_price(self):
        data = {
            'room_type_id': 1,
            'value': 150.00,
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertEqual(BasePrice.objects.get().value, 150.00)

    def test_delete_base_price(self):
        response = self.client.delete(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        self.assertEqual(BasePrice.objects.count(), 0)


class TestRoomTypeBasePrices(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.base_price = BasePrice.objects.create(
            room_type_id=1, value=100, start_date='2023-01-01', end_date='2023-12-31')
        self.url = reverse('base-price-room-type',
                           args=[self.base_price.room_type_id])

    def test_get_base_prices_by_room_type_id(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = BasePriceSerializer(self.base_price)

        self.assertEqual(BasePriceSerializer(
            response.data[0]).data, serializer.data)
