# Converts user-defined currencies using Google
import webbrowser, os, selenium
from selenium import webdriver

driver = webdriver.Firefox()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

currencyX = input("Original Currency: ")
currencyYname = input("Output Currency: ")

currencyX_value = input("Value in " + currencyX + ": ")
URL = 'https://www.google.com/search?client=firefox-b-d&q=' + currencyX_value + ' ' + currencyX + ' to ' + currencyYname
driver.get(URL)
goal = driver.find_element_by_class_name('SwHCTb')
currencyY = goal.text

print('Value in ' + currencyYname + ': ' + currencyY)