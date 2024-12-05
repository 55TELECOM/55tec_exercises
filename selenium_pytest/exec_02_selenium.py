from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pytest

class WebdriverConfig:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def abrir_site(self, url):
        self.webdriver.get(url)
            
    def click_element(self, locator):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).click()
        
    def send_keys(self, locator):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).send_keys("Python Selenium")
    
    def pesquisar_enter(self, locator):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(Keys.ENTER)
    
def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    browser = WebdriverConfig(driver)
    browser.abrir_site("https://www.google.com")
    browser.click_element("//textarea[contains(@id,'APjFqb')]")
    browser.send_keys("//textarea[contains(@id,'APjFqb')]")
    browser.pesquisar_enter("//textarea[contains(@id,'APjFqb')]")
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()