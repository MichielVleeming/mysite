from django.db import models
import datetime
# Create your models here.
from django.db import models
from django.utils import timezone



class Arduino(models.Model):
    arduino_name = models.CharField(max_length=200)
    def __str__(self):
        return self.arduino_name


class MoistureMeter(models.Model):
    arduino = models.ForeignKey(Arduino, on_delete=models.CASCADE)
    moisture_measurement = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.arduino.arduino_name
