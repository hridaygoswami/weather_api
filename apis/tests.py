# from django.test import TestCase

# Create your tests here.

import requests

# url = "https://api.weatherapi.com/v1/current.json?key=75f11d524d2749e4beb110806231909&q=India"
url = "https://api.first.org/data/v1/countries"

response = requests.get(url)

data = response.json()

# for i in data:
#     print(i)
# print(data['data']['DZ']['country'])
c_l = []
for i in data['data']:
    c_l.append(data['data'][str(i)]['country'])

print(c_l)