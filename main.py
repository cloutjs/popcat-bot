from selenium import webdriver
from os import system
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
#options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
browser.get("https://popcat.click/")
time.sleep(2)

clicks = 0
ee = 0
print("clicking...")
while (ee < 3):
    e = browser.find_element_by_xpath("/html")
    e.send_keys(Keys.RETURN)
    clicks = clicks + 1
    system("title " + f"{clicks} clicks")
    time.sleep(1)
