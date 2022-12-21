
#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74452078/selenium-trying-to-figure-out-how-to-loop-through-job-search-on-linkedin-and-sc

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
#All are optional
options.add_experimental_option("detach", True)
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
options.add_argument("--disable-Advertisement")
options.add_argument("--disable-popup-blocking")
options.add_argument("start-maximized")

s=Service('./chromedriver')
driver= webdriver.Chrome(service=s,options = options)


driver.get('https://www.linkedin.com/')
time.sleep(4)

username = driver.find_element(By.CSS_SELECTOR,'#session_key')
username.send_keys('your email')
time.sleep(1)

passward = driver.find_element(By.CSS_SELECTOR,'#session_password')
passward.send_keys('your password')
time.sleep(1)

signin = driver.find_element(By.XPATH,'//*[@class="sign-in-form__submit-button"]').click()
time.sleep(1)

data = []

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3354951485&geoId=103644278&keywords=Software%20Engineer&location=United%20States&refresh=true')
time.sleep(5)

jobs_block = driver.find_element(By.CSS_SELECTOR,'.scaffold-layout__list-container')
jobs_list= jobs_block.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
    
for job in jobs_list:
    a = job.find_element(By.XPATH,'.//*[@class="disabled ember-view job-card-container__link job-card-list__title"]')
    title = a.text if a else None
    print(title)
        
    driver.execute_script("arguments[0].scrollIntoView();", job)