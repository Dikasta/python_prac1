import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoBrowserMethods():
    def find_element_by_id_and_name(self):
        driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        driver.get("https://www.yatra.com/")
        print(driver.current_url)
        driver.find_element(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[2]").click()
        driver.back()
        driver.maximize_window()
        driver.forward()
        driver.back()
        driver.find_element(By.XPATH, "//span[normalize-space()='Visa']").click()
        driver.refresh()
        print(driver.title)
        time.sleep(5)
        driver.quit()
        # time.sleep(5)
        #

demo = DemoBrowserMethods()
demo.find_element_by_id_and_name()


#dsfgjd