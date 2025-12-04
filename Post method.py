import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "first post",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())