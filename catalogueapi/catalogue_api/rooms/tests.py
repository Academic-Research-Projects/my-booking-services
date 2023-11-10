from django.test import Client, TestCase
from django.urls import reverse
from http import HTTPStatus
import json

from room_types.models import RoomType
from hotels.models import Hotel
from .serializers import RoomSerializer
from .models import Room

# Create your tests here.


class TestRooms(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('rooms')
        # creation of an hotel for testing
        self.hotel = Hotel.objects.create(
            name='Test Hotel', address='123 Main St', phone='123-456-7890')
        # creation of a room type for testing
        self.room = RoomType.objects.create(
            name='Test Room Type', capacity=2)

    # test get list of rooms
    def test_list_rooms(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    # test create room
    def test_add_room(self):
        data = {
            'hotel_id': 1,
            'number': 101,
            'room_type_id': 1
        }
        response = self.client.post(self.url, data, format='json')

        # assert that the response status code is equal to 201
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        # assert that the room was created
        self.assertEqual(Room.objects.count(), 1)
        # assert that the room created is equal to the data sent in the request
        self.assertEqual(Room.objects.get().number, 101)


class TestRoom(TestCase):

    def setUp(self):
        self.client = Client()
        # creation of an hotel for testing
        self.hotel = Hotel.objects.create(
            name='Test Hotel', address='123 Main St', phone='123-456-7890')
        # creation of a room type for testing
        self.room = RoomType.objects.create(
            name='Test Room Type', capacity=2)
        # creation of a room for testing
        self.room = Room.objects.create(
            hotel_id=1, number=101, room_type_id=1)
        # pass the room id to the url like this: /rooms/1/
        self.url = reverse('room', args=[self.room.pk])

    # test get room by id
    def test_get_room(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = RoomSerializer(self.room)
        # assert that the response data is equal to the test room created above
        self.assertEqual(response.data, serializer.data)

    # test update room
    def test_update_room(self):
        # new number to update the room
        data = {
            'hotel_id': 1,
            'number': 102,
            'room_type_id': 1
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.room.refresh_from_db()
        # assert that the room updated is equal to the data sent in the request
        self.assertEqual(self.room.number, 102)

    # test delete room
    def test_delete_room(self):
        response = self.client.delete(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        # assert that the room was deleted
        self.assertEqual(Room.objects.count(), 0)
