from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^temperature/$', views.temperature_now, name='temperature_now'),
]
