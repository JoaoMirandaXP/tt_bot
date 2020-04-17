import time
from selenium import webdriver

browse = webdriver.Chrome()

browse.get('https://www.google.com')
time.sleep(10)