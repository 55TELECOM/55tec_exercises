from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import pytest
import time

class WebDriverConfig:
    def __init__(self, webdriver):
        self.webdriver = webdriver
       
    def get_url(self, url):
        self.webdriver.get(url)

    def select_day(self, select_friday):
        select_info = WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, select_friday)))
        select_pos = Select(select_info)
        select_pos.select_by_visible_text("Tuesday")

    def verify_day(self, verify_locator):
        try:
            day_info = WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, verify_locator))).text
            print(day_info)
        except:
            print("O dia selecionado está incorreto!")
def main():
    driver = webdriver.Chrome()
    open_browser = WebDriverConfig(driver)
    url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"
    open_browser.get_url(url)
    select_locator = "//select[contains(@id,'select-demo')]"
    open_browser.select_day(select_locator)
    verify_day_locator = "//p[@class='selected-value text-size-14'][contains(.,'Day selected :- Friday')]"
    open_browser.verify_day(verify_day_locator)
    
    




if __name__ == "__main__":
    main()