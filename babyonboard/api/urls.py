from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^temperature/$', views.temperature, name='temperature'),
    url(r'^temperature/(?P<year>[0-9]{4})/$', views.temperature_year_archive),
    url(r'^temperature/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.temperature_month_archive),
    url(r'^temperature/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.temperature_day_archive),

    url(r'^heartbeats/$', views.heartbeats, name='heartbeats'),
    url(r'^heartbeats/(?P<year>[0-9]{4})/$', views.heartbeats_year_archive),
    url(r'^heartbeats/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.heartbeats_month_archive),
    url(r'^heartbeats/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.heartbeats_day_archive),

    url(r'^breathing/$', views.breathing_now, name='breathing_now'),
    url(r'^breathing/(?P<year>[0-9]{4})/$', views.breathing_year_archive),
    url(r'^breathing/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.breathing_month_archive),
    url(r'^breathing/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.breathing_day_archive),

    url(r'^movement/$', views.movement, name='movement'),

	url(r'^streaming/$', views.streaming, name='streaming'),
]
