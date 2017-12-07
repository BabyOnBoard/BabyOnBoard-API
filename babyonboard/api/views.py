import json
import os
import datetime
import pytz
from random import *
from subprocess import Popen
from django.http import HttpResponse, JsonResponse
from django.utils.dateparse import parse_datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Temperature, HeartBeats, Breathing, BabyCrib, Noise, Movement
from .utils import runCScript
from .serializers import TemperatureSerializer, HeartBeatsSerializer, BreathingSerializer, BabyCribSerializer, NoiseSerializer, MovementSerializer


# Temperature endpoint
@api_view(['GET', 'POST'])
def temperature(request):
    if request.method == 'GET':
        temperature = Temperature.objects.order_by('datetime').last()
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'temperature': request.data.get('temperature')
        }
        serializer = TemperatureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Heartbeats endpoint
@api_view(['GET', 'POST'])
def heartbeats(request):
    if request.method == 'GET':
        heartbeats = HeartBeats(beats=randint(50, 110))
        serializer = HeartBeatsSerializer(heartbeats)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'beats': request.data.get('beats')
        }
        serializer = HeartBeatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Breathing endpoint
@api_view(['GET', 'POST'])
def breathing(request):
    if request.method == 'GET':
        breathing = Breathing.objects.order_by('datetime').last()
        serializer = BreathingSerializer(breathing)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'status': request.data.get('status')
        }
        serializer = BreathingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Movement endpoint
@api_view(['GET', 'POST'])
def movement(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        now = pytz.utc.localize(now).timestamp()
        babycrib = BabyCrib.objects.order_by('datetime').last()
        if babycrib is None:
            movement = Movement(is_moving=False, remaining_time=0, movement='resting')
            serializer = MovementSerializer(movement)
            return Response(serializer.data, status=status.HTTP_200_OK)
        time_difference = now - babycrib.datetime.timestamp()
        if time_difference > babycrib.duration * 60:
            movement = Movement(is_moving=False, remaining_time=0, movement='resting')
            serializer = MovementSerializer(movement)
            return Response(serializer.data, status=status.HTTP_200_OK)
        time_remaining = (babycrib.duration * 60) - time_difference
        movement = Movement(is_moving=True, remaining_time=time_remaining, movement=babycrib.status)
        serializer = MovementSerializer(movement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        movement = request.data.get('status')
        if (movement.lower(), movement.title()) in BabyCrib.MOVEMENT_CHOICES:
            data = {
                'status': movement,
                'duration': request.data.get('duration')
            }
            serializer = BabyCribSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                script_path = os.path.abspath(__file__ + '/../scripts/movimento')
                movement_id = get_id(movement)
                Popen(['sudo ./home/pi/Git/BabyOnBoard-Sensores/motor', str(movement_id), str(duration)])
                return Response(data=None, status=status.HTTP_201_CREATED)
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)


# Streaming endpoint
@api_view(['POST'])
def streaming(request):
    action = request.data.get('action')
    if action == 'restart' or action == 'start' or action == 'stop':
        script_path = os.path.abspath(__file__ + '/../scripts/motioncontrol.py')
        os.system("python {} {}".format(script_path, action))
        return Response(data=None, status=status.HTTP_200_OK)
    return Response(data=None, status=status.HTTP_400_BAD_REQUEST)


# Noise endpoint
@api_view(['GET', 'POST'])
def noise(request):
    if request.method == 'GET':
        noise = Noise.objects.order_by('datetime').last()
        serializer = NoiseSerializer(noise)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'is_crying': request.data.get('is_crying')
        }
        serializer = NoiseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_id(movement):
    if movement == 'side':
        return 1
    elif movement == 'front':
        return 2
    elif movement == 'vibration':
        return 3
    else:
        return 0


@api_view(['GET'])
def is_moving(request):
    now = datetime.datetime.now()
    now = pytz.utc.localize(now).timestamp()
    movement = BabyCrib.objects.order_by('datetime').last()
    if movement is None:
        return Response(data=None, status=status.HTTP_200_OK)
    time_difference = now - movement.datetime.timestamp()
    if time_difference > movement.duration * 60:
        data = {
            'movement': 'resting',
            'is_moving': False,
            'time_remaining': 0
        }
        return Response(data=data, status=status.HTTP_200_OK)
    time_remaining = time_difference - (movement.duration * 60)
    data = {
        ''
        'is_moving': True,
        'time_remaining': time_remaining
    }
    return Response(data=data, status=status.HTTP_200_OK)
