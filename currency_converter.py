# Converts user-defined currencies using Google
import webbrowser, bs4, requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

currencyX = input("Original Currency: ")
currencyYname = input("Output Currency: ")

currencyX_value = input("Value in " + currencyX + ": ")
URL = 'https://www.google.com/search?client=firefox-b-d&q=' + currencyX_value + ' ' + currencyX + ' to ' + currencyYname
res = requests.get(URL, headers=headers)
soup = bs4.BeautifulSoup(res.text, features="lxml")
currencyY = soup.select('span.DFlfde.SwHCTb')
currencyY_value = round(float(currencyY[0].get('data-value')), 2)

formatted_currencyY = ("{:,}".format(currencyY_value))

print('Value in ' + currencyYname + ': ' + formatted_currencyY)