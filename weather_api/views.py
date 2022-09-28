from django.shortcuts import render
import requests

def index(request):
    """
    index def for response api weather
    """
    api_url = "http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    city_name = 'Yemen'

    url = api_url+city_name
    response = requests.get(url)
    content = response.json()

    city_weather = {
        'city': city_name,
        'temperature': content['main']['temp'],
        'description': content['weather'][0]['description'],
        'icon': content['weather'][0]['icon']
    }
    return render(request, 'weather.html', {'city_weather': city_weather})

