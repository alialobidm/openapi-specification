# [START maps_http_geocode_components]
import requests

url = "https://maps.googleapis.com/maps/api/geocode/json?components=locality%3Asanta%20cruz%7Ccountry%3AES&key=YOUR_API_KEY"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# [END maps_http_geocode_components]