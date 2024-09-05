import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import geocoder as geocoder
import requests
from .models import Worldcities

# Create your views here.
def temp_somewhere(request):
	random_item = Worldcities.objects.all().order_by('?').first()
	city = random_item.city
	location = [random_item.lat, random_item.lng]
	temp = get_temp(location)
	template = loader.get_template('index.html')
	context = {
		'city': city,
		'temp': temp
	}
	return HttpResponse(template.render(context, request))

def temp_here(request):
	location = geocoder.ip('me').latlng
	temp = get_temp(location)
	template = loader.get_template("index.html")
	context = {
		'city': 'Atlanta',
		'temp': temp
	}
	return HttpResponse(template.render(context, request))

def get_temp(location):
	endpoint = "https://api.open-meteo.com/v1/forecast"
	api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
	now = datetime.datetime.now()
	hour = now.hour
	meteo_data = requests.get(api_request).json()
	temp = meteo_data['hourly']['temperature_2m'][hour]
	return temp