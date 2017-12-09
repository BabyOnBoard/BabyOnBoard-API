from django.db import models


class Temperature(models.Model):
    """
    Temperature Model
    Defines the atributes of a temperature registry obtained from sensor
    """
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.temperature)


class HeartBeats(models.Model):
    """
    HeartBeats Model
    Defines the atributes of a heartbeats registry obtained from sensor
    """
    beats = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.beats)


class Breathing(models.Model):
    """
    Breathing Model
    Defines the atributes of a breathing registry obtained from sensor
    """
    ABSENT = 'absent'
    BREATHING = 'breathing'
    NO_BREATHING = 'no_breathing'

    BREATHING_CHOICES = (
        (ABSENT, 'Absent'),
        (BREATHING, 'Breathing'),
        (NO_BREATHING, 'No Breathing'),
    )

    status = models.CharField(
        max_length=15,
        choices=BREATHING_CHOICES,
        default=ABSENT
    )

    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.status)


class BabyCrib(models.Model):
    """
    BabyCrib Model
    Defines the atributes of the babycrib
    """
    RESTING = 'resting'
    FRONT = 'front'
    SIDE = 'side'
    VIBRATION = 'vibration'

    MOVEMENT_CHOICES = (
        (RESTING, 'Resting'),
        (FRONT, 'Front'),
        (SIDE, 'Side'),
        (VIBRATION, 'Vibration'),
    )

    status = models.CharField(
        max_length=10,
        choices=MOVEMENT_CHOICES,
        default=RESTING
    )

    duration = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.status)


class Movement(models.Model):
    """
    Movement Model
    Defines if the baby crib is moving, and the remaining time
    """
    is_moving = models.BooleanField()
    remaining_time = models.IntegerField()
    movement = models.CharField(max_length=10, default='resting')

    def __str__(self):
        return str(self.is_moving)

    def get_movement_id(movement):
        if movement == 'front':
            return 1
        elif movement == 'side':
            return 2
        elif movement == 'vibration':
            return 3
        else:
            return 0


class Noise(models.Model):
    """
    Noise Model
    Defines if the baby is crying or not
    """
    is_crying = models.BooleanField()
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.is_crying)
