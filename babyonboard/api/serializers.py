from rest_framework import serializers
from .models import Temperature, HeartBeats, Breathing, BabyCrib, Noise


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('__all__')


class HeartBeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartBeats
        fields = ('__all__')


class BreathingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breathing
        fields = ('__all__')


class BabyCribSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyCrib
        fields = ('__all__')


class NoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noise
        fields = ('__all__')
