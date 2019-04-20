from rest_framework import serializers
from .models import Arduino,MoistureMeter

class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Arduino
       fields = ('id','name')

    def create(self, validated_data):
        return Arduino.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance