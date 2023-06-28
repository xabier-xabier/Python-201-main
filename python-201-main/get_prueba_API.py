import requests
from pprint import pprint

#params={ "email":"ryan@codingnomads.co"}
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
#response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users",params=params)
#print(response.status_code)

#pprint(response.json())

response=requests.get(base_url)

print(response.status_code)
print(response.text)
print(response.headers)