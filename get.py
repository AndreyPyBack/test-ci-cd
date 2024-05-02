import requests


url = 'http://127.0.0.1:8000/api/cars/1'
response = requests.get(url)
print(response.status_code)
print(response.json())
