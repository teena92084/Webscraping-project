from pprint import pprint
import json
a=open('Movies_Detail.json',"r")
r=a.read()
movie_list=json.loads(r)
print(movie_list)


def group_by_year():
    year_list=[]
    dict={}
    for movie in movie_list:
        year=movie["year_of_release"]
        movie_list2=[]
        if year not in year_list:
            year_list.append(year)
            for movie1 in movie_list:
                if movie1["year_of_release"]==year:
                    movie_list2.append(movie1)
                else:
                    pass
            dict[year]=movie_list2
    return dict  

movie_dict=group_by_year()    

with open ("Task2.json","w") as f:
    k=json.dump(movie_dict,f,indent=4)