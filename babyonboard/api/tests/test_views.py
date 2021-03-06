import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Temperature, HeartBeats, Breathing, BabyCrib, Movement, Noise
from ..serializers import TemperatureSerializer, HeartBeatsSerializer, BreathingSerializer, BabyCribSerializer, MovementSerializer, NoiseSerializer


client = Client()


class GetCurrentTemperatureTest(TestCase):
    """ Test class for GET current temperature from API """

    def setUp(self):
        Temperature.objects.create(temperature=35)

    def test_get_current_temperature(self):
        response = client.get(reverse('temperature'))
        temperature = Temperature.objects.order_by('datetime').last()
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
        heartbeats = HeartBeats.objects.order_by('datetime').last()
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

    def test_create_invalid_heartbeats(self):
        response = client.post(
            reverse('heartbeats'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetCurrentBreathingTest(TestCase):
    """ Test class for GET current breathing from API """

    def setUp(self):
        Breathing.objects.create(status=1)

    def test_get_current_breathing(self):
        response = client.get(reverse('breathing'))
        breathing = Breathing.objects.order_by('datetime').last()
        serializer = BreathingSerializer(breathing)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewBreathingTest(TestCase):
    """" Test class for saving a new breathing registry """

    def setUp(self):
        self.valid_payload = {
            'status': 'breathing'
        }
        self.invalid_payload = {
            'status': 'crying'
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


class GetBabyCribStatusTest(TestCase):
    """ Test class to check babycrib status """

    def setUp(self):
        BabyCrib.objects.create(status='vibration', duration=100)

    def test_get_babycrib_status(self):
        response = client.get(reverse('movement'))
        babycrib = BabyCrib.objects.order_by('datetime').last()
        serializer = BabyCribSerializer(babycrib)
        self.assertEqual(response.data['movement'], serializer.data['status'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_still_moving_registry(self):
        response = client.get(reverse('movement'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_moving'], True)
        self.assertTrue(response.data['remaining_time'] > 0)

    def test_get_empty_babycrib_registry(self):
        BabyCrib.objects.all().delete()
        response = client.get(reverse('movement'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_moving'], False)   


class ControlBabyCribMovementTest(TestCase):
    """ Test class for controling babycrib movementation """

    def setUp(self):
        self.valid_payload = {
            'status': 'resting',
            'duration': '0'
        }
        self.invalid_payload = {
            'status': 'stop',
            'duration': 100
        }

    def test_set_invalid_movement(self):
        response = client.post(
            reverse('movement'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_raise_file_not_found(self):
        response = client.post(
            reverse('movement'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetCurrentNoiseStatusTest(TestCase):
    """ Test class for GET current crying status from API """

    def setUp(self):
        Noise.objects.create(is_crying=True)

    def test_get_movement_status(self):
        response = client.get(reverse('noise'))
        noise = Noise.objects.order_by('datetime').last()
        serializer = NoiseSerializer(noise)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewNoiseTest(TestCase):
    """" Test class for saving a new noise registry """

    def setUp(self):
        self.valid_payload = {
            'is_crying': True
        }
        self.invalid_payload = {
            'is_crying': 'crying'
        }

    def test_create_valid_noise(self):
        response = client.post(
            reverse('noise'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_noise(self):
        response = client.post(
            reverse('noise'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
