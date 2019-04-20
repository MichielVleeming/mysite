from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('arduinos/', views.arduino_list),
    path('arduinos/<int:pk>', views.arduino_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)