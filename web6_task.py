import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
adventure_movies_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
top_movies_api=requests.get(adventure_movies_url)
soup=BeautifulSoup(top_movies_api.text,"html.parser")
div=soup.find("table",class_="table")
tr=div.find_all("tr")
movies_no=[]
for i in tr:
    tbody=i.find_all("td",class_="bold")
    for j in tbody:
        serial_no=j.get_text()
        movies_no.append(serial_no)
        # print(serial_no)
    movies_rea=[]
    for k in tbody:
        reating=i.find("span",class_="tMeterScore").get_text()
        movies_rea.append(reating)
        # print(movies_rea)
    movies_name1=[]
    for l in tbody:
        movies_name=i.find("a",class_="unstyled articleLink").get_text()
        movies_name1.append(movies_name)
        # print(movies_name1)
    top_movies=[]
    for n in tbody:
        movies_name=i.find("a",class_="unstyled articleLink").get_text()

        split_year=movies_name.split()
        slic=split_year[-1][1:5]
        top_movies.append(slic)
        # print(top_movies)
    movies=[]
    for m in tbody:
        movies_url=i.find("a",class_="unstyled articleLink")['href']
        movies_link="https://www.rottentomatoes.com/"+movies_url
        movies.append(movies_link)
        # print(movies)
        
        deaitals={"movies_no":serial_no,"movies_rea":reating,"movies_name1":movies_name,"top_movies":slic,"movies":movies_link}
        top_movies.append(deaitals)
        with open ("top_movies.json","w") as f:
            json.dump(top_movies,f,indent=4)
    # pprint(top_movies)



        
