from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from parsel import Selector
from .models import Employee


def login(driver, username, password):
    """
    Utility function to login to linkedin.
    """
    driver.get('https://www.linkedin.com/login')
    
    # Email
    email_elem = driver.find_element_by_id('username')
    email_elem.send_keys(username)
    # Password
    password_elem = driver.find_element_by_id('password')
    password_elem.send_keys(password)
    # Enter
    password_elem.send_keys(Keys.ENTER)

def scroll_to_bottom(driver):
    """
    Utility function to scroll linkedin page till bottom.
    """
    try:
        time.sleep(0.5)
        for scroll in range(30):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1.5)
        time.sleep(0.5)
    except TimeoutException as e:
        print(str(e))
        raise ValueError('Took too long to scroll page.')

def clean_name(name):
    """Name is extracted from the title thats why it has some unwanted substrings from title in linked page.
        To remove those we use below code"""
    substring_list = [
        '(', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')']
    for substring in substring_list:
        name = name.replace(substring, '')
        name = name.strip()
    return name

def scrap_profiles(driver):
    """
    select the profile from the webpage and scrap it.
    """
    try:
        sel = Selector(text=driver.page_source)
        name = sel.xpath(
            '//title/text()').extract_first().split(' | ')[0]
        name = clean_name(name)
        job_title = sel.xpath('//h2/text()').getall()[1]
        ln_url = driver.current_url

        # upsert to Employee Model
        name = name[1:]
        Employee.objects.get_or_create(
        name=name.strip(),
        designation=job_title.strip(),
        company='Mambu')
        time.sleep(5)
    except:
        print('failed to scrape profile')

def get_profile(profile, driver):
    """
    Load the profile link and scrap it
    """
    try:
        driver.get(profile)
        scrap_profiles(driver)
    except TimeoutException as e:
        print(str(e))
        raise ValueError('Took too long to scroll page.')


def get_profiles_link_and_scrap_profiles(driver):
    """
    get the list of all profiles and scrap each profile one by one.
    """
    unique_profiles_list = []
    profiles = driver.find_elements_by_xpath('//a[1]')
    profiles = [profile.get_attribute(
        'href') for profile in profiles if 'https://www.linkedin.com/in/' in profile.get_attribute('href')]
    # # avoid first two links as its loggedin users links
    profiles = profiles[2:]
    # # remove duplicate links if any
    list_set = set(profiles)
    # # convert the set to the list
    unique_profiles_list = (list(list_set))
    if len(unique_profiles_list):
        for profile in unique_profiles_list:
            get_profile(profile, driver)

