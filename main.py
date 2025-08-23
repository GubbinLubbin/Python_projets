import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
html=requests.get(url=URL)
soup=BeautifulSoup(html.text,"html.parser")
List= soup.find("div", attrs={"class": "gallery", "data-template-type": "inline"}).find_all("h3",attrs={"class":"title"})
# for elements in List:
#     print(elements.get_text())
with open("best_movies.txt","w") as file:
    for elements in List:
        file.write(f"{elements.get_text()}\n)")
        
