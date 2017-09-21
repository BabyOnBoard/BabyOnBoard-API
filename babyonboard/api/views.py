from django.http import HttpResponse
from .models import Temperature, HeartBeats, Breathing, BabyCrib
from .utils import jsonify


JSON_CONTENT = 'application/json'

def temperature_now(request):
    temperature = Temperature.objects.order_by('date', 'time').last()
    content = jsonify(temperature)

    return HttpResponse(content, JSON_CONTENT)

def heartbeats_now(request):
    heartbeats = HeartBeats.objects.order_by('date', 'time').last()
    content = jsonify(heartbeats)

    return HttpResponse(content, JSON_CONTENT)

def breathing_now(request):
    breathing = Breathing.objects.order_by('date', 'time').last()
    content = jsonify(breathing)

    return HttpResponse(content, JSON_CONTENT)

def movement_now(request):
    babycrib = BabyCrib.objects.order_by('date', 'time').last()
    content = jsonify(babycrib)

    return HttpResponse(content, JSON_CONTENT)
