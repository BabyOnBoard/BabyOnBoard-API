import json
import os
from random import choice
from django.http import HttpResponse, JsonResponse
from .models import Temperature, HeartBeats, Breathing, BabyCrib
from .utils import jsonify
from .utils import runCScript
from .serializers import TemperatureSerializer, HeartBeatsSerializer, BreathingSerializer, BabyCribSerializer


# Temperatures endpoints
def temperature_now(request):
    temps = []
    x = 35.9
    y = 0.1
    for t in range(0, 30):
        x += y
        temps.append(round(x, 1))
    temperature = Temperature(temperature=choice(temps))
    temperature.save()
    # temperature = Temperature.objects.order_by('date', 'time').last()
    serializer = TemperatureSerializer(temperature)
    return JsonResponse(serializer.data)

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
def heartbeats_now(request):
    beats = []
    for b in range(50, 101):
        beats.append(b)
    heartbeats = HeartBeats(beats=choice(beats))
    heartbeats.save()
    # heartbeats = HeartBeats.objects.order_by('date', 'time').last()
    serializer = HeartBeatsSerializer(heartbeats)
    return JsonResponse(serializer.data)

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
def breathing_now(request):
    breathings = [True, False]
    breathing = Breathing(is_breathing=choice(breathings))
    breathing.save()
    # breathing = Breathing.objects.order_by('date', 'time').last()
    serializer = BreathingSerializer(breathing)
    return JsonResponse(serializer.data)

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

def movement_now(request):
    babycrib = BabyCrib.objects.order_by('date', 'time').last()
    serializer = BabyCribSerializer(babycrib)
    return JsonResponse(serializer.data)

def movement(request):
    if request.method == 'POST':
        return movement_set(request)
    elif request.method == 'GET':
        return movement_now(request)

    return HttpResponse('', status=405, reason='Method not allowed, only GET or POST.')


# Streaming endpoint
def streaming(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        action = body["action"]
        script_path = os.path.abspath(__file__ + "/../scripts/motioncontrol.py")
        os.system("python3 {} {}".format(script_path, action))
        return HttpResponse('', status=200)

    return HttpResponse('', status=405, reason='Method not allowed, only POST.')

# Private Methods

def movement_set(request):
    # parsing body to json

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    movement_type = body["type"]

    duration = body["duration"]

    if movement is "vertical":
        runCScript(movement_type)
        print("Setting movement to - VERTICAL " + movement_type + " " + duration)
    if movement is "horizontal":
        runCScript(movement_type)
        print("Setting movement to - HORIZONTAL" + movement_type + " " + duration)
    if movement is "vibrate":
        runCScript(movement_type)
        print("Setting movement to - VIBRATE" + movement_type + " " + duration)


    # Make python code to summon a C executable or a shell script that does it
    return HttpResponse('', status=200)
