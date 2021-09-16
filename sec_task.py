from web7_task import*
import json
def relese_yr():
    year=[]
    for i in movies_data():
        for j in i:
            if i["top_movies"] not in year:
                year.append(i["top_movies"])
    year=sorted(year)
    movie_dict={i:[]for i in year}
    for i in movies_data():
        yr=i["top_movies"]
        for x in movie_dict:
            if str(x)==str(yr):
                movie_dict[x].append(i)
    
        with open("avenger_task.json","w")as f:
            json.dump(movie_dict,f,indent=2)
    return movie_dict

relese_yr()