from django.conf.urls import url
from hava.views import WeatherSituationView

urlpatterns = [
	url(r'^current-weather/$', WeatherSituationView.as_view(), name='SendCurrentWeather'),
	]
