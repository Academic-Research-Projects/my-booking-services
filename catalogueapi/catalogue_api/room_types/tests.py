from django.test import Client, TestCase
from django.urls import reverse
from http import HTTPStatus
import json

from .serializers import RoomTypeSerializer
from .models import RoomType

# Create your tests here.


class TestRoomTypes(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('room-types')

    # test get list of room_types
    def test_get_room_types(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    # test create room_type
    def test_post_room_type(self):
        data = {
            'name': 'test room type',
            'capacity': 2
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        self.assertEqual(RoomType.objects.count(), 1)

        self.assertEqual(RoomType.objects.get().capacity, 2)


class TestRoomType(TestCase):

    def setUp(self):
        self.client = Client()

        self.room_type = RoomType.objects.create(
            name='Test Room Type', capacity=2)

        self.url = reverse('room-type', args=[self.room_type.pk])

    # test get room type by id
    def test_get_room_type_by_id(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = RoomTypeSerializer(self.room_type)

        self.assertEqual(response.data, serializer.data)

    # test update room type

    def test_update_room_type(self):
        data = {
            'name': 'Test Room Type',
            'capacity': 3
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.room_type.refresh_from_db()
        self.assertEqual(self.room_type.capacity, 3)

    # test delete room
    def test_delete_room_type(self):
        response = self.client.delete(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        self.assertEqual(RoomType.objects.count(), 0)
