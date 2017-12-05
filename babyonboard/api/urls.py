from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^temperature/$', views.temperature, name='temperature'),
    url(r'^heartbeats/$', views.heartbeats, name='heartbeats'),
    url(r'^breathing/$', views.breathing, name='breathing'),
    url(r'^movement/$', views.movement, name='movement'),
    url(r'^is_moving/$', views.is_moving, name='is_moving'),
    url(r'^streaming/$', views.streaming, name='streaming'),
    url(r'^noise/$', views.noise, name='noise'),
]
