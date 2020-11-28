# import requests
# import json

# url = "https://yandex.ru/images/search?text=cats"
# response = requests.get(url)
# data = response.json()
# my_json = response.content
# print(first_img)
# print(my_json)
# data = json.loads(my_json)
# print(data)
# s = json.dumps(data, indent=4, sort_keys=True)
# print(s)
# if response.status_code == 200:
#     with open("./sample.jpg", 'wb') as f:
#         f.write(response.content)

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=котики&source=lnms&tbm=isch'

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')


for raw_img in soup.find_all('img'):
    link = raw_img.get('src')
    if link and link.startswith('https'):
        response = requests.get(link)
        with open("./today_avatar.jpg", 'wb') as f:
            f.write(response.content)
        break