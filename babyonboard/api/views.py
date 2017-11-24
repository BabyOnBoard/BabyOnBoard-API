import json
import os
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Temperature, HeartBeats, Breathing, BabyCrib
from .utils import runCScript
from .serializers import TemperatureSerializer, HeartBeatsSerializer, BreathingSerializer, BabyCribSerializer


# Temperature endpoints
@api_view(['GET', 'POST'])
def temperature(request):
    if request.method == 'GET':
        temperature = Temperature.objects.order_by('date', 'time').last()
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

def temperature_year_archive(request, year):
    temperatures = Temperature.objects.filter(date__year=year)
    serializer = TemperatureSerializer(temperatures, many=True)
    return JsonResponse(serializer.data, safe=False)

def temperature_month_archive(request, year, month):
    temperatures = Temperature.objects.filter(date__year=year, date__month=month)
    serializer = TemperatureSerializer(temperatures, many=True)
    return JsonResponse(serializer.data, safe=False)

def temperature_day_archive(request, year, month, day):
    temperatures = Temperature.objects.filter(date__year=year, date__month=month, date__day=day)
    serializer = TemperatureSerializer(temperatures, many=True)
    return JsonResponse(serializer.data, safe=False)

# Heartbeats endpoints
@api_view(['GET', 'POST'])
def heartbeats(request):
    if request.method == 'GET':
        heartbeats = HeartBeats.objects.order_by('date', 'time').last()
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

def heartbeats_year_archive(request, year):
    heartbeats = HeartBeats.objects.filter(date__year=year)
    serializer = HeartBeatsSerializer(heartbeats, many=True)
    return JsonResponse(serializer.data, safe=False)

def heartbeats_month_archive(request, year, month):
    heartbeats = HeartBeats.objects.filter(date__year=year, date__month=month)
    serializer = HeartBeatsSerializer(heartbeats, many=True)
    return JsonResponse(serializer.data, safe=False)

def heartbeats_day_archive(request, year, month, day):
    heartbeats = HeartBeats.objects.filter(date__year=year, date__month=month, date__day=day)
    serializer = HeartBeatsSerializer(heartbeats, many=True)
    return JsonResponse(serializer.data, safe=False)

# Breathing endpoints
@api_view(['GET', 'POST'])
def breathing(request):
    if request.method == 'GET':
        breathing = Breathing.objects.order_by('date', 'time').last()
        serializer = BreathingSerializer(breathing)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'is_breathing': request.data.get('is_breathing')
        }
        serializer = BreathingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def breathing_year_archive(request, year):
    breathings = Breathing.objects.filter(date__year=year)
    serializer = BreathingSerializer(breathings, many=True)
    return JsonResponse(serializer.data, safe=False)

def breathing_month_archive(request, year, month):
    breathings = Breathing.objects.filter(date__year=year, date__month=month)
    serializer = BreathingSerializer(breathings, many=True)
    return JsonResponse(serializer.data, safe=False)

def breathing_day_archive(request, year, month, day):
    breathings = Breathing.objects.filter(date__year=year, date__month=month, date__day=day)
    serializer = BreathingSerializer(breathings, many=True)
    return JsonResponse(serializer.data, safe=False)

# Movement endpoints
@api_view(['GET', 'POST'])
def movement(request):
    if request.method == 'GET':
        babycrib = BabyCrib.objects.order_by('date', 'time').last()
        serializer = BabyCribSerializer(babycrib)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'status': request.data.get('status'),
            'duration': request.data.get('duration')
        }
        serializer = BabyCribSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            runCScript(data['status'], data['duration'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Streaming endpoint
@api_view(['POST'])
def streaming(request):
    action = request.data.get('action')
    if action == 'restart' or action == 'start' or action == 'stop':
        script_path = os.path.abspath(__file__ + '/../scripts/motioncontrol.py')
        os.system("python {} {}".format(script_path, action))
        return Response(data=None, status=status.HTTP_200_OK)
    return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
