import requests
from requests.exceptions import HTTPError
import json

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print('Success')
elif response.status_code == 404:
    print('Not Found')

# Another way to write the test to verify
# It is important to understand that here __bool() is an overloaded method because of response
# Here Responses takes the status code into account when determining the truth value of the
# object
if response:
    print("Success")
else:
    raise Exception(f"Something went wrong: {response.status_code}")

# Another way "use raise for status()"

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")

# Test to Verify the Payload and Using JSON Loads
# Remember there is a difference between load and Loads
response = requests.get("https://api.github.com")
# .content gives you the raw bytes of the response payload
print(response.content)
print(type(response.content))

print(response.text)
print(type(response.text))

# So decoding of bytes to a str requires an encoding
response.encoding = "utf-8"
print(response.text)
print(type(response.text))

# Now using to get serialized JSON Content
print(response.json())
print(type(response.json()))
response_dict = response.json()
print(response_dict["emojis_url"])

# This is the Metadata about the response
response = requests.get("https://api.github.com")
print(response.headers)
print(response.headers["Content-Type"])

