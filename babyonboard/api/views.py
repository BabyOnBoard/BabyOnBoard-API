from django.http import HttpResponse
from .models import Temperature, HeartBeats, Breathing, BabyCrib
from .utils import jsonify
from django.core import serializers
import json


JSON_CONTENT = 'application/json'

def temperature_now(request):
    temperature = Temperature.objects.order_by('date', 'time').last()
    temperature = [temperature, ]
    # content = jsonify(temperature)
    # serialize queryset
    if temperature is None:
        temperature = []
    serialized_queryset = serializers.serialize('json', temperature)

    # serialize object
    return HttpResponse(serialized_queryset, JSON_CONTENT)

def heartbeats_now(request):
    heartbeats = HeartBeats.objects.order_by('date', 'time').last()
    content = jsonify(heartbeats)

    return HttpResponse(content, JSON_CONTENT)

def breathing_now(request):
    breathing = Breathing.objects.order_by('date', 'time').last()
    content = jsonify(breathing)

    return HttpResponse(content, JSON_CONTENT)

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
        print("Setting movement to - VERTICAL " + movement_type + " " + duration)
    if movement is "horizontal":
        print("Setting movement to - HORIZONTAL" + movement_type + " " + duration)
    if movement is "vibrate":
        print("Setting movement to - VIBRATE" + movement_type + " " + duration)


    # Make python code to summon a C executable or a shell script that does it
    return HttpResponse('', status=200)


def movement_now(request):
    babycrib = BabyCrib.objects.order_by('date', 'time').last()
    content = jsonify(babycrib)
    return HttpResponse(content, JSON_CONTENT)