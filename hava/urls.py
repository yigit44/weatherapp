from django.conf.urls import url
from hava.views import WeatherSituationView
from . import views

urlpatterns = [
	url(r'^current-weather/$', WeatherSituationView.as_view(), name='SendCurrentWeather'),
	]
