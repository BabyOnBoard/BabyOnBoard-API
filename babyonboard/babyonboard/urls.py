from django.conf.urls import url, include
from django.contrib import admin
from api import urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('api.urls')),
]
