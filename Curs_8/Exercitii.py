import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Checkboxes").click()
time.sleep(2)
chrome.find_elements(By.TAG_NAME, "input")[0].click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, "Context").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, "Content").click()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "click here").click()
time.sleep(2)
chrome.back()
chrome.back()
time.sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, "Download").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
time.sleep(2)
chrome.find_element(By.ID, "username").send_keys("tom-smith")
time.sleep(2)
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(2)
chrome.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Forgot Password").click()
time.sleep(2)
chrome.find_element(By.NAME, "email").send_keys("marius1979@yahoo.com")
time.sleep(2)
chrome.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Frames").click()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "iFrame").click()
time.sleep(2)
chrome.find_element(By.CLASS_NAME, "tox-mbtn__select-label").click()
time.sleep(2)
chrome.find_element(By.CLASS_NAME, "tox-collection__item-label").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Inputs").click()
time.sleep(2)
chrome.find_element(By.TAG_NAME, "input").send_keys("1")
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Key Presses").click()
time.sleep(2)
chrome.find_element(By.ID, "target").send_keys("abc")
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Horizontal Slider").click()
time.sleep(2)
chrome.find_element(By.TAG_NAME, "input").click()
time.sleep(2)
chrome.back()
time.sleep(2)

chrome.maximize_window()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(2)
chrome.find_element(By.ID, "ez-accept-all").click()
time.sleep(2)
chrome.find_element(By.NAME, "firstname").send_keys("Claudia")
time.sleep(2)
chrome.find_element(By.NAME, "lastname").send_keys("Marcu")
time.sleep(2)

chrome.maximize_window()
chrome.get("https://jules.app/sign-in")
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input').send_keys("abc@yahoo.com")
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input').send_keys("abcd")
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button').click()
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/a').click()
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/div/input').send_keys("abc@yahoo.com")
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/button/span[1]').click()
time.sleep(2)
chrome.back()
time.sleep(2)
