from bs4 import BeautifulSoup
import csv
import requests

url = 'https://www.imdb.com/chart/top/'
source = requests.get(url).text

# file opening
csv_file = open('imdb_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Movie Name', 'Release Year', 'Movie Rating'])

soup = BeautifulSoup(source, 'lxml')
title_col = soup.find_all('td', class_='titleColumn')
rating_col = soup.find_all('td', class_='ratingColumn imdbRating')