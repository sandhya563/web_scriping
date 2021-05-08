import requests
import json
from bs4 import BeautifulSoup
from task1 import scrap_top_list


def group_by_year(movies):
    dic = {}
    for i in movies:
        movie_data = []
        for j in movies:
            if i["year"] == j["year"]:
                movie_data.append(i)
                dic[i["year"]] = movie_data

    with open("task2.json","w+") as data_file:
        json.dump(dic,data_file,indent=4)

group_by_year(movies=scrap_top_list())
