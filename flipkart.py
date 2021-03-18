from bs4 import BeautifulSoup
import requests
from requests_html import HTML, HTMLSession



session = HTMLSession()

r = requests.get("https://www.flipkart.com/search?q=bags&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1")

src = r.content
soup = BeautifulSoup(src,'html.parser')


div = soup.find_all('div',class_='_2WkVRV')
for i in div:
    print(i)

link = soup.find_all('a',class_='IRpwTa')
for iter in link:
    print(iter.attrs['href'])

images = soup.find_all('img')
for img in images:
    print('image',img)