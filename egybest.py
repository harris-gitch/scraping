from distutils.filelist import findall
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

movies=[]
titles=[]
rating=[]
links=[]
result = requests.get("https://hola.egybest.asia/trending/")

src =result.content

soup = BeautifulSoup(src,"lxml")
#print(soup)
movie= soup.find_all("a",{"class":"movie"})
#print(movie)
movie_rate=soup.find_all("i",{"class":"i-fav rating"})
movie_name=soup.find_all("span",{"class":"title"})


for i in range(len(movie)):
   movies.append(movie[i].attrs["href"])
   titles.append(movie_name[i].text)
   rating.append(movie_rate[i].text)
#print(movies)
for link in movies:
   result = requests.get(link)
   src =result.content
   soup = BeautifulSoup(src,"lxml")
   linkm= soup.find("iframe",{"class":"auto-size"})
   links.append(linkm.attrs["src"])
#print(links)

file_list=[titles,rating,links]
exported= zip_longest(*file_list)
with open("/home/linux-user/Desktop/python/result.csv","w") as myfile :
    wr = csv.writer(myfile)
    wr.writerow(["titles","rating","link"])
    wr.writerows(exported)
