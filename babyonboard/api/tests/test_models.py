from django.test import TestCase
from ..models import Temperature, HeartBeats, Breathing, BabyCrib


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


class BreathingTest(TestCase):
    """Test class for breathing model"""

    def setUp(self):
        Breathing.objects.create(is_breathing=True)

    def test_create_breathing(self):
        breathing = Breathing.objects.get(is_breathing=True)
        self.assertIsNotNone(breathing)
        self.assertTrue(isinstance(breathing, Breathing))
        self.assertEqual(breathing.__str__(), str(breathing.is_breathing))


class BabyCribTest(TestCase):
    """Test class for babycrib model"""

    def setUp(self):
        BabyCrib.objects.create(status='resting', duration=0)

    def test_create_breathing(self):
        babycrib = BabyCrib.objects.get(status='resting')
        self.assertIsNotNone(babycrib)
        self.assertTrue(isinstance(babycrib, BabyCrib))
        self.assertEqual(babycrib.__str__(), str(babycrib.status))
