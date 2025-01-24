
import requests
url = "https://api.github.com/repos/JKronick/test/contents"

response = requests.get(url)

contents = response.json()

for content in contents:
    print(content["name"])
    print(content["sha"])