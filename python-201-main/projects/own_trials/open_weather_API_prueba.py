
import requests
from pprint import pprint

lat=0.4535757794231666
lon=101.45313303258905
limit=5

API_key="ab429330748f508db5b61e5e5e22dfd1"

#url=f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_key}"

#base_url=f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API_key}"
base_url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"


response = requests.get(base_url)
resp_lan=response.json()

print((resp_lan["weather"][0]["main"]))
