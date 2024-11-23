import requests

# endpoint = "https://httpbin.org"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "salsdfsdfom"})
# get_response = requests.post(endpoint, params={"abc": 123}, data={'aasda':'asdsad'}, json={"sdfgdfg": "salsdfsdfom"})

print(get_response.headers)
print(get_response.text)
# print(get_response.json())
print(get_response.status_code)