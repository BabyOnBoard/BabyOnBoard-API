from django.db import models


class Temperature(models.Model):
    """
    Temperature Model
    Defines the atributes of a temperature registry obtained from sensor
    """
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.temperature)


class HeartBeats(models.Model):
    """
    HeartBeats Model
    Defines the atributes of a heartbeats registry obtained from sensor
    """
    beats = models.PositiveIntegerField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

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

    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

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
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.status)


class Noise(models.Model):
    """
    Noise Model
    Defines if the baby is crying or not
    """
    is_crying = models.BooleanField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.is_crying)
