import requests

url = "http://localhost:8000/api/v1/generate-description"

payload = {
    "input_code": "def hello_world():\n    print('Hello, world!')"
}

response = requests.post(url, json=payload)
print(response.json())

