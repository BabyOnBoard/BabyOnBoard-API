from django.test import TestCase
from ..models import Temperature, HeartBeats, Breathing, BabyCrib, Movement, Noise


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
        Breathing.objects.create(status='no_breathing')

    def test_create_breathing(self):
        breathing = Breathing.objects.get(status='no_breathing')
        self.assertIsNotNone(breathing)
        self.assertTrue(isinstance(breathing, Breathing))
        self.assertEqual(breathing.__str__(), str(breathing.status))


class BabyCribTest(TestCase):
    """Test class for babycrib model"""

    def setUp(self):
        BabyCrib.objects.create(status='resting', duration=0)

    def test_create_babycrib(self):
        babycrib = BabyCrib.objects.get(status='resting')
        self.assertIsNotNone(babycrib)
        self.assertTrue(isinstance(babycrib, BabyCrib))
        self.assertEqual(babycrib.__str__(), str(babycrib.status))


class MovementTest(TestCase):
    """Test class for movement model"""

    def setUp(self):
        Movement.objects.create(is_moving=True, remaining_time=30, movement='front')
        Movement.objects.create(is_moving=True, remaining_time=50, movement='side')
        Movement.objects.create(is_moving=True, remaining_time=60, movement='vibration')
        Movement.objects.create(is_moving=False, remaining_time=0, movement='resting')

    def test_create_movement(self):
        movement = Movement.objects.get(movement='front')
        self.assertIsNotNone(movement)
        self.assertTrue(isinstance(movement, Movement))
        self.assertEqual(movement.__str__(), str(movement.is_moving))

    def test_get_movement_id(self):
        front_movement = Movement.objects.get(movement='front')
        side_movement = Movement.objects.get(movement='side')
        vibration_movement = Movement.objects.get(movement='vibration')
        resting_movement = Movement.objects.get(movement='resting')
        self.assertEqual(1, Movement.get_movement_id(front_movement.movement))
        self.assertEqual(2, Movement.get_movement_id(side_movement.movement))
        self.assertEqual(3, Movement.get_movement_id(vibration_movement.movement))
        self.assertEqual(0, Movement.get_movement_id(resting_movement.movement))


class NoiseTest(TestCase):
    """Test class for noise model"""

    def setUp(self):
        Noise.objects.create(is_crying=False)

    def test_create_noise(self):
        noise = Noise.objects.get(is_crying=False)
        self.assertIsNotNone(noise)
        self.assertTrue(isinstance(noise, Noise))
        self.assertEqual(noise.__str__(), str(noise.is_crying))
