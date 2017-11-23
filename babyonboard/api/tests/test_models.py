from django.test import TestCase
from ..models import Temperature


class TemperatureTest(TestCase):
    """Test class for temperature model"""

    def setUp(self):
        Temperature.objects.create(temperature=20.5)

    def test_create_temperature(self):
        temperature = Temperature.objects.get(temperature=20.5)
        self.assertIsNotNone(temperature)
        self.assertTrue(isinstance(temperature, Temperature))
        self.assertEqual(temperature.__str__(), str(temperature.temperature))
