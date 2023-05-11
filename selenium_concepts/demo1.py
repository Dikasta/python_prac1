import time

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class DemoBrowserMethods():
    def find_element_by_id_and_name(self):
        driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
        driver.get("https://selectorshub.com/")
        driver.find_element(By.XPATH,"(//a[@class='hfe-menu-item'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//li[@id='menu-item-2279']").click()
        driver.execute_script("window.scrollTo(0,400)")  # scroll tab in mid level of page
        time.sleep(2)
        driver.find_element(By.XPATH,"(//span[text()='Install'])[1]").click()
        time.sleep(5)





demo=DemoBrowserMethods()
demo.find_element_by_id_and_name()

#dfgnjf
