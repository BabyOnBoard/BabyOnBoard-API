import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Temperature, HeartBeats, Breathing
from ..serializers import TemperatureSerializer, HeartBeatsSerializer, BreathingSerializer


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


class GetCurrentHeartBeatsTest(TestCase):
    """ Test class for GET current heartbeats from API """

    def setUp(self):
        HeartBeats.objects.create(beats=70)

    def test_get_current_heartbeats(self):
        response = client.get(reverse('heartbeats'))
        heartbeats = HeartBeats.objects.order_by('date', 'time').last()
        serializer = HeartBeatsSerializer(heartbeats)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewHeartBeatsTest(TestCase):
    """" Test class for saving a new heartbeats registry """

    def setUp(self):
        self.valid_payload = {
            'beats': 80
        }
        self.invalid_payload = {
            'beats': ''
        }

    def test_create_valid_heartbeats(self):
        response = client.post(
            reverse('heartbeats'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_temperature(self):
        response = client.post(
            reverse('heartbeats'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetCurrentBreathingTest(TestCase):
    """ Test class for GET current breathing from API """

    def setUp(self):
        Breathing.objects.create(is_breathing=True)

    def test_get_current_breathing(self):
        response = client.get(reverse('breathing'))
        breathing = Breathing.objects.order_by('date', 'time').last()
        serializer = BreathingSerializer(breathing)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewBreathingTest(TestCase):
    """" Test class for saving a new breathing registry """

    def setUp(self):
        self.valid_payload = {
            'is_breathing': True
        }
        self.invalid_payload = {
            'is_breathing': ''
        }

    def test_create_valid_breathing(self):
        response = client.post(
            reverse('breathing'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_breathing(self):
        response = client.post(
            reverse('breathing'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ControlStreamingTest(TestCase):
    """ Test class for starting or stoping streaming """

    def setUp(self):
        self.valid_payload = {
            'action': 'start'
        }
        self.invalid_payload = {
            'action': 'continue'
        }

    def test_valid_streaming_control(self):
        response = client.post(
            reverse('streaming'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_streaming_control(self):
        response = client.post(
            reverse('streaming'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
