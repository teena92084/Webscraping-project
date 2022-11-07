from Task2 import movie_dict
from pprint import pprint
import json
def group_by_decade():
   
    moviedec={}
    list1=[]
    for i in movie_dict:
        
        i=int(i)
        mode=i%10
        decade=i-mode
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movie_dict:
            x=(x)
            if x<=dec10 and x>=i:
                for v in movie_dict[x]:
                    moviedec[i].append(v)
    with open("Task3.json","w") as a:

        json.dump(moviedec, a,indent=6)

    return moviedec


decade=group_by_decade()