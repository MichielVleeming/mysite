from django.http import HttpResponse
from django.urls import path
from . import views
from .models import MoistureMeter

def index(request):
    latest_measurement_list = MoistureMeter.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.arduino.arduino_name for q in latest_measurement_list])
    return HttpResponse(output)

def detail(request, arduino_id):
    return HttpResponse("You're looking at arduino %s." % arduino_id)

def measurement(request, arduino_id):
    response = "The measurements are %s."
    return HttpResponse(response % arduino_id)