import requests
import json
from bs4 import BeautifulSoup

task1_file_ = open("task1.json")
task1_data = json.load(task1_file_)

task2_file = open("task2.json")
task2_data = json.load(task2_file)

def group_by_decade():
    decade_year = []
    movie_di = {}
    for i in task2_data:
        year = i
        mod = int(year)%10
        decade = int(year)-mod
        if decade not in decade_year:
            decade_year.append(decade)
        decade_year.sort()
    print(decade_year)

    i = 0
    movie_dic = {}
    while i<len(decade_year):
        value = decade_year[i]+10
        list1 = []
        for j in task2_data:
            if int(j) >= decade_year[i] and int(j) <= value:
                list1.append(task2_data[j])
        movie_dic[decade_year[i]] = list1
        i=i+1
    print(movie_dic)

    with open("task3.json","w+") as data_file:
        json.dump(movie_dic,data_file,indent=4)
    print(movie_dic)

group_by_decade()
