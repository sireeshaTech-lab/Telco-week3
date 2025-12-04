import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

data = response.json()

print("JSON Data:")
print(data)