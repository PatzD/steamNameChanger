from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.options import Options

import time

binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

firefox_options = Options()
firefox_options.binary_location = binary_path

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://steamcommunity.com/login/home/?goto=")

time.sleep(15)

user = "zak132465"

driver.get(f"https://steamcommunity.com/id/{user}/edit/info")
name_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div/div[3]/div[3]/div[2]/form/div[3]/div[2]/div[1]/label/div[2]/input")
save_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div/div[3]/div[3]/div[2]/form/div[7]/button[1]")

with open("bee_movie.txt", "r") as file:
    for line in file:
        words = line.split(" ")
        for word in words:
            name_box.clear()
            name_box.send_keys(word)
            save_button.click()
            time.sleep(1)


time.sleep(3)
driver.close()
