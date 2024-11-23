import requests

endpoint = "http://localhost:8000/api/products/2"

get_response = requests.get(endpoint, json={"title": "salsdfsdfom"})

# print(get_response.headers)
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)