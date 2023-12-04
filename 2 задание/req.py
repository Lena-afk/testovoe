import requests

url = "http://localhost:5000/api/data"
data = {"key1": "your_kafka_topic", "key2": "value2"}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
