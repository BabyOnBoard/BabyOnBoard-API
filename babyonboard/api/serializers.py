from rest_framework import serializers
from .models import Temperature, HeartBeats, Breathing, BabyCrib


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id', 'temperature', 'date', 'time')


class HeartBeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartBeats
        fields = ('id', 'beats', 'date', 'time')


class BreathingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breathing
        fields = ('id', 'is_breathing', 'date', 'time')


class BabyCribSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyCrib
        fields = ('id', 'duration', 'date', 'time')
