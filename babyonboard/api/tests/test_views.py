import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Temperature
from ..serializers import TemperatureSerializer


client = Client()


class GetCurrentTemperatureTest(TestCase):
    """ Test class for GET current temperature from API """

    def setUp(self):
        Temperature.objects.create(temperature=35)

    def test_get_current_temperature(self):
        response = client.get(reverse('temperature'))
        temperature = Temperature.objects.order_by('date', 'time').last()
        serializer = TemperatureSerializer(temperature)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewTemperatureTest(TestCase):
    """ Test class for saving a new temperature registry """

    def setUp(self):
        self.valid_payload = {
            'temperature': 27.2
        }

        self.invalid_payload = {
            'temperature': ''
        }

    def test_creat_valid_temperature(self):
        response = client.post(
            reverse('temperature'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_temperature(self):
        response = client.post(
            reverse('temperature'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
