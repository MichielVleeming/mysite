from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:arduino_id>/', views.detail, name='detail'),
    path('<int:arduino_id>/measurement/', views.measurement,name='measurement'),

]