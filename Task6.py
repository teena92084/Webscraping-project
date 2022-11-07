from Task1 import top_movie
import requests
from bs4 import BeautifulSoup
import json
hh=[]
def  analyse_movies_language(top_movie):
    for i in range(0,51 ):
        a=top_movie[i]["link"]
        d1={}
        u=[]
        page=requests.get(a)
        soup=BeautifulSoup(page.text,'html.parser')
        for ul in soup.find_all('a', class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"):
            u.append(ul.get_text())
        list=["Hindi","English","Tamil","Telugu","Malayalam","Kannada","Bengali","Marathi"]
        for i in u:
            for j in list:
                if i==j:
                 hh.append(i)
    print(hh)
    i=0
    k={}
    while i<len(list):
        j=0
        c=0
        while j<len(hh):
            if list[i]==hh[j]:
                c=c+1
            k[list[i]]=c
            j=j+1
        print()
        i=i+1
    return k
b=analyse_movies_language(top_movie)
with open("Task6.json","w")as h:
    d=json.dump(b,h,indent=2)