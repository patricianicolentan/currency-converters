# Converts USD to PHP using Google
import webbrowser, bs4, requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


USD_value = input("USD: ")
URL = 'https://www.google.com/search?client=firefox-b-d&q=' + USD_value + ' usd+to+php'
res = requests.get(URL, headers=headers)
soup = bs4.BeautifulSoup(res.text, features="lxml")
PHP = soup.select('span.DFlfde.SwHCTb')
PHP_value = round(float(PHP[0].get('data-value')), 2)

formatted_PHP = ("{:,}".format(PHP_value))

print("PHP: " + formatted_PHP)
