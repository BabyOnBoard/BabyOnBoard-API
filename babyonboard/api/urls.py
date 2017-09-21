from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^temperature/$', views.temperature_now, name='temperature_now'),
    url(r'^heartbeats/$', views.heartbeats_now, name='heartbeats_now'),
]
