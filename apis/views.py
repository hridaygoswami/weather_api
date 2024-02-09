from django.shortcuts import render
import requests
from django import forms 
from .models import Countries
# Create your views here.

class Country(forms.Form):
    country_name = forms.CharField(max_length=120)

def index(request):
    url = "https://api.first.org/data/v1/countries"
    response = requests.get(url)

    data = response.json()
    country_name = [] 
    for i in data['data']:
        country_name.append(data['data'][str(i)]['country'])
    return render(request, "index.html", {
        "form":Country,
        "countries":country_name
    })

def country(request):
    data = request.POST
    print(data['country_list'])
    cname = data['country_list']
    url = f"https://api.weatherapi.com/v1/current.json?key=75f11d524d2749e4beb110806231909&q={cname}"
    response = requests.get(url).json()
    temp_c = response['current']['temp_c']
    temp_f = response['current']['temp_f']
    c = Countries(country_name=cname, temp_cm=temp_c, temp_fm=temp_f)
    c.save()
    return render(request, "new.html", {
        "c":temp_c,
        "f":temp_f,
        "cname":cname
    })
