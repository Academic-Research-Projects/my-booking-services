from http import HTTPStatus
import json
from django.test import Client, TestCase
from django.urls import reverse

from .serializers import PriceVariationSerializer

from .models import PriceVariation

# Create your tests here.


class TestPriceVariations(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.url = reverse('price-variations')

    def test_list_price_variations(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_price_variation(self):
        data = {
            'base_price_id': 1,
            'variation': 10.00,
            'day': 0
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, HTTPStatus.CREATED)


class TestPriceVariation(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.price_variation = PriceVariation.objects.create(
            base_price_id=1, variation=10.00, day=0)
        self.url = reverse('price-variation', args=[self.price_variation.pk])

    def test_get_price_variation_by_id(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = PriceVariationSerializer(self.price_variation)

        self.assertEqual(response.data, serializer.data)

    def test_update_price_variation(self):
        data = {
            'base_price_id': 1,
            'variation': 20.00,
            'day': 0
        }
        response = self.client.put(self.url, json.dumps(
            data), content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertEqual(PriceVariation.objects.get().variation, 20.00)

    def test_delete_price_variation(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

        self.assertEqual(PriceVariation.objects.count(), 0)


class TestBasePricePriceVariations(TestCase):
    def setUp(self):  # this method is called before each test
        self.client = Client()
        self.price_variation = PriceVariation.objects.create(
            base_price_id=1, variation=10.00, day=0)
        self.url = reverse(
            'price-variation-base-price', args=[self.price_variation.base_price_id])

    def test_get_price_variations_by_base_price(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        serializer = PriceVariationSerializer(self.price_variation)

        self.assertEqual(response.data[0], serializer.data)
