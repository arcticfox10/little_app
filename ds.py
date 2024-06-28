import requests


url=f'https://kidkodschool.github.io/welcome.html'

respose=requests.get(url)
print(respose.content)