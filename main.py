from bs4 import BeautifulSoup
import requests

r = requests.get(url='https://www.filmweb.pl/ranking/film').text
soup = BeautifulSoup(r, 'html.parser')
movie_list = soup.find_all(name='h2', class_="rankingType__title")
titles = [str(movie_list.index(title) + 1) + ") " + title.text for title in movie_list]
with open('movies.txt', mode='w', encoding="utf-8") as movies:
    for m in titles:
        movies.write(m + "\n")
