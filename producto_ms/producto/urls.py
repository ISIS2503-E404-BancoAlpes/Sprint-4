from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^productos/', views.MeasurementList),
    url(r'^productocreate/$', csrf_exempt(views.MeasurementCreate), name='measurementCreate'),
    url(r'^productoupdate/$', csrf_exempt(views.MeasurementsCreate), name='createMeasurements'),
]