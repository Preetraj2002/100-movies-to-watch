import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url=URL)
website_content=response.text

soup=BeautifulSoup(website_content,"html.parser")

# print(soup.prettify())
movies=[movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()

print(movies)
with open(file="movies.txt",mode="w",encoding="utf") as fw:
    for movie in movies:
        fw.write(movie+"\n")
