import requests
import json
city = 'delhi'#input("enter the city name : ")
url = f'http://api.weatherapi.com/v1/current.json?key=898b6dd60f3c4aaaa0e161220252701&q={city}'
api = requests.get(url)
wread = json.loads(api.text)
print(wread['current']['temp_c'])
