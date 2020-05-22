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

def scrap_profiles(driver):
    """
    select the profile from the webpage and scrap it.
    """
    try:
        sel = Selector(text=driver.page_source)
        root = driver.find_element_by_class_name("pv-top-card")
        name = root.find_elements_by_xpath("//section/div/div/div/*/li")[0].text.strip()
        job_title = sel.xpath('//h2/text()').getall()[1]
        ln_url = driver.current_url

        # upsert to Employee Model
        Employee.objects.get_or_create(
        name=name,
        designation=job_title.strip(),
        company='Mambu')
        time.sleep(5)
    except:
        print('failed to scrape profile')
        pass

def get_profiles_link_and_scrap_profiles(driver):
    """
    get the list of all profiles and scrap each profile one by one.
    """
    profiles = driver.find_elements_by_xpath('//a[@data-control-name="people_profile_card_image_link"]')

    profiles = [profile.get_attribute('href') for profile in profiles if 'https://www.linkedin.com/in/' in profile.get_attribute('href')]

    for profile in profiles:
            driver.get(profile)
            scrap_profiles(driver)
