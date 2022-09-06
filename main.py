from bs4 import BeautifulSoup
import csv
import requests

url = 'https://www.imdb.com/chart/top/'
source = requests.get(url).text