from bs4 import BeautifulSoup
import csv
import requests

url = 'https://www.imdb.com/chart/top/'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')
title_col = soup.find_all('td', class_='titleColumn')
rating_col = soup.find_all('td', class_='ratingColumn imdbRating')