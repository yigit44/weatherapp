import requests
from django.shortcuts import render
from django.conf import settings

from rest_framework.generics import GenericAPIView



# Create your views here.
class WeatherSituationView(GenericAPIView):
	def post(self):
		city_name = self.request.data.get('city')
		weather_url = settings.OPEN_WEATHER_API
		params = {
			'q'= city_name,
  			'appid'= '0fa71fc77f705bab55a6027f6e1e5995'
		}
		r = requests.get(weather_url, params=params)
		json_object = r.json()
		temp_k = float(json_object['main']['temp'])
		return temp_k