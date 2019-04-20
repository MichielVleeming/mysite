from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import MoistureMeter, Arduino

admin.site.register(MoistureMeter)
admin.site.register(Arduino)