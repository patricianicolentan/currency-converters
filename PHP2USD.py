# Converts PHP to USD using Google
import webbrowser, bs4, requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


PHP_value = input("PHP: ")
URL = 'https://www.google.com/search?client=firefox-b-d&q=' + PHP_value + ' php+to+usd'
res = requests.get(URL, headers=headers)
soup = bs4.BeautifulSoup(res.text, features="lxml")
USD = soup.select('span.DFlfde.SwHCTb')
USD_value = round(float(USD[0].get('data-value')), 2)

formatted_USD = ("{:,}".format(USD_value))

print("USD: " + formatted_USD)
