import requests

url = "http://127.0.0.1:8000/items/"
payload = {
    "name": "Car",
    "description": "Doug's Car",
    "price": 1.50,
    "tax": 1
}

res = requests.post(url json=payload)
print("Status", res.status_code)
print("Response:", res.json())
