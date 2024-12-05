from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time


class WebDriverConfig:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def get_url(self, url):
        self.webdriver.get(url)

    def verify_title(self, title):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_all_elements_located((By.XPATH, title)))
            print(f'O titulo é Example Domain')
        except:
            print('O titulo está errado!')
    
    def click_element(self, click_locator, verify_locator):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, click_locator))).click()
    
    def verify_window(self, window):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, window)))
        except:
            print('A página não foi aberta!')



def main():
    driver = webdriver.Chrome()
    open_browser = WebDriverConfig(driver)
    url1 = "https://example.com"
    open_browser.get_url(url1)
    title = "//h1[contains(.,'Example Domain')]"
    open_browser.verify_title(title)
    driver.switch_to.new_window('window')
    driver.set_window_position(950, 0)
    url2 = "https://the-internet.herokuapp.com/windows"
    open_browser.get_url(url2)
    click_locator = "//a[contains(.,'Click Here')]"
    verify_locator = "//h3[contains(.,'New Window')]"
    open_browser.click_element(click_locator)
    driver.switch_to.window(driver.window_handles[-1])
    open_browser.verify_window(verify_locator)
    time.sleep(2)

if __name__ == "__main__":
    main()