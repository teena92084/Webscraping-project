from bs4 import BeautifulSoup
from Task1 import top_movie
import requests
import json
def get_movie_list_details(move_list):
    i=0
    g=[]

    while i<=5:
        d=move_list[i]["link"]
        d1={}
        u=[]
        page=requests.get(d)
        soup=BeautifulSoup(page.text,'html.parser')
        movie=soup.find("div",class_="sc-80d4314-0 fjPRnj").h1.get_text()
        d1["movie_name"]=movie
        for ul in soup.find_all('a', class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"):
          u.append(ul.get_text())
        list=["Hindi","English","Tamil","Telugu","Malayalam","Kannada","Bengali"]
        hh=[]
        for k in u:
            for l in list:
                if k==l:
                    hh.append(k)
        d1["language"]=hh
        runtime=soup.find("div",class_="sc-80d4314-2 iJtmbR").get_text().strip()
        u=runtime[-6:]
        d1["Runtime"]=[u]
        bio=soup.find("div",class_="sc-16ede01-7 hrgVKw").get_text()
        d1["bio"]=[bio]
        director=soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
        d1["Director"]=[director]
        poster_image=soup.find("div",class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img").img['src']
        d1["postername"]=poster_image
        abc=soup.find('div',class_="ipc-chip-list__scroller")
        ga=abc.find('span')
        list1=[]
        for j in ga:
            list1.append(j)
            d1['genre']=list1
        Detail=soup.find("section",cel_widget_id="StaticFeature_Details")
        s=Detail.find_all("div")
        y=[]
        for ul in s:
                h=ul.find_all("ul")
                for li in h:
                    o=li.find_all("li")
                    for aa in o:
                        z=aa.find_all('a')
                        details=[details.get_text() for details in z]
                        for p in details:
                            y.append(p)
        d1["country"]=y[5]
        b=y[1].split()
        d1["release_year"]=b[2]
        d1["release_date"]=b[1]+b[0]
        i=i+1
        g.append(d1)
    return g
sss=get_movie_list_details(top_movie)
with open("Task5.json","w")as h:
        s=json.dump(sss,h,indent=2)