from django.http import HttpResponse
from .models import Temperature
from .utils import jsonify


JSON_CONTENT = 'application/json'

def temperature_now(request):
    temperature = Temperature.objects.order_by('date', 'time').last()
    content = jsonify(temperature)

    return HttpResponse(content, JSON_CONTENT)
