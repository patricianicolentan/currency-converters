# Converts PHP to USD using Google
import webbrowser, os, selenium
from selenium import webdriver

driver = webdriver.Firefox()


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Gets user-input PHP value
PHP_value = input('PHP: ')

# Declares URL and gets the converted result
URL = 'https://www.google.com/search?client=firefox-b-d&q=' + PHP_value + ' php+to+usd'
driver.get(URL)
goal = driver.find_element_by_class_name('SwHCTb')
USD = goal.text

# Prints the converted result
print('USD: ' + USD)