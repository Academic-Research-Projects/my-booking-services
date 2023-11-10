from http import HTTPStatus
import json
from django.test import Client, TestCase
from django.urls import reverse

from .models import HotelOption

# Create your tests here.


class TestHotelOptions(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.url = reverse('hotel-options')

    def test_list_hotel_options(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_hotel_option(self):
        data = {
            'hotel_id': 1,
            'number': 1,
            'option_type': 'PS'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, HTTPStatus.CREATED)


class TestHotelOption(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.hotel_option = HotelOption.objects.create(
            hotel_id=1, number=1, option_type='PS')
        self.url = reverse('hotel-option', args=[self.hotel_option.pk])

    def test_get_hotel_option(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_update_hotel_option(self):
        data = {
            'hotel_id': 1,
            'number': 2,
            'option_type': 'PS'
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertEqual(HotelOption.objects.get().number, 2)

    def test_delete_hotel_option(self):
        response = self.client.delete(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        self.assertEqual(HotelOption.objects.count(), 0)
