import os
import requests
from lxml import html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configparser import ConfigParser


driver = webdriver.Chrome('../linkedin_scraper/chromedriver_linux64/chromedriver')

# Loading of configurations
config = ConfigParser()
config.read('../config.ini')
username = config.get('linkedin', 'username')
password = config.get('linkedin', 'password')


class Scraper(object):
    driver = None

    def is_signed_in(self):
        try:
            self.driver.find_element_by_id("profile-nav-item")
            return True
        except:
            pass
        return False

    def __find_element_by_class_name__(self, class_name):
        try:
            self.driver.find_element_by_class_name(class_name)
            return True
        except:
            pass
        return False

    def __find_element_by_xpath__(self, tag_name):
        try:
            self.driver.find_element_by_xpath(tag_name)
            return True
        except:
            pass
        return False

    def __find_element_by_id_name__(self, id_name):
        try:
            self.driver.find_element_by_id_name(id_name)
            return True
        except:
            pass
        return False


class Person(Scraper):
    __TOP_CARD = "pv-top-card"
    name = None
    linkedin_url = None
    location = None

    def __init__(self, linkedin_url=None, name=None, driver=None, get=True, scrape=True):
        self.linkedin_url = linkedin_url
        self.name = name

        if driver is None:
            driver = webdriver.Chrome('../linkedin_scraper/chromedriver_linux64/chromedriver')

        if get:
            driver.get(linkedin_url)

        self.driver = driver

        if scrape:
            self.scrape()

    def add_location(self, location):
        self.location=location
    
    def scrape(self, close_on_complete=True):
        if self.is_signed_in():
            self.scrape_logged_in(close_on_complete = close_on_complete)
        else:
            self.scrape_not_logged_in(close_on_complete = close_on_complete)

    def scrape_logged_in(self, close_on_complete=True):
        driver = self.driver
        root = driver.find_element_by_class_name(self.__TOP_CARD)
        self.name = root.find_elements_by_xpath("//section/div/div/div/*/li")[0].text.strip()

        # get location
        location = driver.find_element_by_class_name(f'{self.__TOP_CARD}--list-bullet')
        location = location.find_element_by_tag_name('li').text
        self.add_location(location)

        if close_on_complete:
            driver.close()


    def scrape_not_logged_in(self, close_on_complete=True, retry_limit=10):
        driver = self.driver
        retry_times = 0
        while self.is_signed_in() and retry_times <= retry_limit:
            page = driver.get(self.linkedin_url)
            retry_times = retry_times + 1

        # get name
        self.name = driver.find_element_by_id("name").text.strip()

        # get
        if close_on_complete:
            driver.close()

    def __repr__(self):
        return "{name} \n {location} \n {linkedin_url}".format(name = self.name, location=self.location, linkedin_url=self.linkedin_url)


# Login on linkedin
def login(driver, email=None, password=None):
  driver.get("https://www.linkedin.com/login")
  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

  email_elem = driver.find_element_by_id("username")
  email_elem.send_keys(email)

  password_elem = driver.find_element_by_id("password")
  password_elem.send_keys(password)
  driver.find_element_by_tag_name("button").click()



login(driver, username, password)
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)
print(person)
