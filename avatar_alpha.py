import requests

from bs4 import BeautifulSoup

url = f'https://www.google.com/search?q=котики&source=lnms&tbm=isch'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

for raw_img in soup.find_all('img'):
    link = raw_img.get('src')
    if link and link.startswith('https'):
        response = requests.get(link)
        with open("./today_avatar.jpg", 'wb') as f:
            f.write(response.content)
        break