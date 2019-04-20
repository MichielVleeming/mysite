from django.db import models

# Create your models here.
from django.db import models


class MoistureMeter(models.Model):
    moisture_measurement = models.IntegerField(default=0)
    arduino_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')