from django.db import models


class Temperature(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.temperature)


class HeartBeats(models.Model):
    beats = models.PositiveIntegerField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.beats)


class Breathing(models.Model):
    is_breathing = models.BooleanField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.is_breathing)


class BabyCrib(models.Model):
    RESTING = 'Resting'
    FRONT = 'Front'
    SIDE = 'Side'
    VIBRATION = 'Vibration'

    MOVEMENT_CHOICES = (
        (RESTING, 'resting'),
        (FRONT, 'front'),
        (SIDE, 'side'),
        (VIBRATION, 'vibration'),
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
