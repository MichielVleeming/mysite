from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Arduino
from .serializers import ArduinoSerializer


@api_view(['GET', 'POST'])
def arduino_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        arduinos = Arduino.objects.all()
        serializer = ArduinoSerializer(arduinos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArduinoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def arduino_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        arduino = Arduino.objects.get(pk=pk)
    except Arduino.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArduinoSerializer(arduino)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArduinoSerializer(arduino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        arduino.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)