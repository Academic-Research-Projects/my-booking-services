from django.test import Client, TestCase
from django.urls import reverse
from http import HTTPStatus
import json

from .serializers import HotelSerializer
from .models import Hotel

# Create your tests here.


class TestHotels(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('hotels')

    # test get list of hotels
    def test_list_hotels(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    # test create hotel
    def test_add_hotel(self):
        data = {
            'name': 'Test Hotel',
            'address': '123 Main St',
            'phone': '123-456-7890'
        }
        response = self.client.post(self.url, data, format='json')

        # assert that the response status code is equal to 201
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        # assert that the hotel was created
        self.assertEqual(Hotel.objects.count(), 1)
        # assert that the hotel created is equal to the data sent in the request
        self.assertEqual(Hotel.objects.get().name, 'Test Hotel')


class TestHotel(TestCase):

    def setUp(self):
        self.client = Client()
        # creation of an hotel for testing
        self.hotel = Hotel.objects.create(
            name='Test Hotel', address='123 Main St', phone='123-456-7890')
        # pass the hotel id to the url like this: /hotels/1/
        self.url = reverse('hotel', args=[self.hotel.pk])

    # test get hotel by id
    def test_get_hotel(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = HotelSerializer(self.hotel)
        # assert that the response data is equal to the test hotel created above
        self.assertEqual(response.data, serializer.data)

    # test update hotel
    def test_update_hotel(self):
        # new phone number to update the hotel
        data = {
            'name': 'Test Hotel',
            'address': '123 Main St',
            'phone': '098-765-4321'
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.hotel.refresh_from_db()
        # assert that the phone number was updated
        self.assertEqual(self.hotel.phone, '098-765-4321')

    def test_delete_hotel(self):
        response = self.client.delete(self.url, format='json')

        # assert that the response status code is equal to 204
        # 204 means that the request was successful but no content was returned
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        # check that the hotel object was deleted
        self.assertEqual(Hotel.objects.count(), 0)
