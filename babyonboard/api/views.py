from django.http import HttpResponse, JsonResponse
from .models import Temperature, HeartBeats, Breathing, BabyCrib
from .utils import jsonify
from .utils import runCScript
from .serializers import TemperatureSerializer, HeartBeatsSerializer, BreathingSerializer
import json


def temperature_now(request):
    temperature = Temperature.objects.order_by('date', 'time').last()
    serializer = TemperatureSerializer(temperature)
    return JsonResponse(serializer.data)

def heartbeats_now(request):
    heartbeats = HeartBeats.objects.order_by('date', 'time').last()
    serializer = HeartBeatsSerializer(heartbeats)
    return JsonResponse(serializer.data)

def breathing_now(request):
    breathing = Breathing.objects.order_by('date', 'time').last()
    serializer = BreathingSerializer(breathing)
    return JsonResponse(serializer.data)

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
