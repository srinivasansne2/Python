#pip install 2captcha-python
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from webdriver_manager.chrome import ChromeDriverManager
#pip install webdriver-manager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://coe1.annauniv.edu/home/')

captcha_img=driver.find_element(By.CLASS_NAME,'small')

captcha_img.screenshot('img/captcha.png')
#print(captcha_img)

api_key=os.getenv('APIKEY_2CAPTCHA','##########Your API HERE############')

solver = TwoCaptcha(api_key)
try:
    result=solver.normal('img/captcha.png')
except Exception as e:
    print(e)
else:
    code=result['code']
    #print(code)
    driver.find_element(By.ID,'register_no').send_keys("812621243052")
    driver.find_element(By.ID,'dob').send_keys("17-04-2004")
    driver.find_element(By.ID,'security_code_student').send_keys(code.upper())
    login=driver.find_elements(By.CLASS_NAME,'buttonSubmit')
    login[1].click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT,'EXAM RESULTS').click()
    print("Finished")