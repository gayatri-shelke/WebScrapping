import requests
from bs4 import BeautifulSoup

song_url="https://en.wikipedia.org/wiki/Category:Hindi_film_songs"
page=requests.get(song_url)
soup=BeautifulSoup(page.text,"html.parser")
main_div=soup.find('div',class_='mw-body')
# title=main_div.find('h1',class_='firstheading')
td=main_div.find('div',class_='mw-category')
k=td.find('div',class_='mw-category-group')
l=k.find('')


# print(k)

# print(437//32)