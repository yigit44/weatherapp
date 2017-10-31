from django.conf.urls import url
from hava.views import WeatherSituationView

urlpatterns = [
	url(r'^$', WeatherSituationView.as_view(), name='post'),
	]
