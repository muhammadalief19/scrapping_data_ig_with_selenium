import pandas as pd
import datetime
import time
import random
import pytz

import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger

logger.add("logs/app.log", level="INFO")
logger.add

pd.set_option('display.max_colwidth', None)

class Processor:
    def __init__(self, user, password):
        self.driver = webdriver.Chrome(r"D:\\membantu-teman\\maksom\\scrapping-ig\\driver\\chromedriver.exe")
        self.user_ig = user
        self.password_ig = password
        self.timesleep = random.randint(5, 10)
        self.postingan_data = []
    
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(self.timesleep)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.clear()
        password.clear()
        username.send_keys(self.user_ig)
        password.send_keys(self.password_ig)
        login = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(self.timesleep)
    
    def to_profile(self, user):
        self.driver.get(f"https://www.instagram.com/{user}/")
        time.sleep(self.timesleep)
    
    def scrapping_ig(self, user, limit):
        self.to_profile(user)
        scrool_limit = limit / 12
        
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_times = 0;
        
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.timesleep)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if ((new_height == last_height) or (scroll_times == scrool_limit)):
                break
            
            elems = len(self.driver.find_elements(By.XPATH,value='//div[@class="_aabd _aa8k _aanf"]/a'))
            logger.info(f"Scrapped {elems} posts")
            
    
    def scrapping_each_postingan(self):
        pass
    
    def scrapping_data_postingan(self):
        pass
    
    def save_data(self):
        data = pd.DataFrame(self.postingan_data)
        data.to_csv(f"{self.user_ig}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", index=False)
        print("Data berhasil disimpan")
    