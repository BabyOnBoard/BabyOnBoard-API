from django.test import TestCase
from ..models import Temperature, HeartBeats


class TemperatureTest(TestCase):
    """Test class for temperature model"""

    def setUp(self):
        Temperature.objects.create(temperature=20.5)

    def test_create_temperature(self):
        temperature = Temperature.objects.get(temperature=20.5)
        self.assertIsNotNone(temperature)
        self.assertTrue(isinstance(temperature, Temperature))
        self.assertEqual(temperature.__str__(), str(temperature.temperature))


class HeartBeatsTest(TestCase):
    """Test class for heartbeats model"""

    def setUp(self):
        HeartBeats.objects.create(beats=70)

    def test_create_heartbeats(self):
        heartBeats = HeartBeats.objects.get(beats=70)
        self.assertIsNotNone(heartBeats)
        self.assertTrue(isinstance(heartBeats, HeartBeats))
        self.assertEqual(heartBeats.__str__(), str(heartBeats.beats))
