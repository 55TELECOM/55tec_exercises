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

    def click_botton(self, locator):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).click()

    def alert_verify(self):
        WebDriverWait(self.webdriver, 3).until((EC.alert_is_present()))

def main():
    driver = webdriver.Chrome()
    open_browser = WebDriverConfig(driver)
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    try:
        locator_js = "//button[@onclick='jsAlert()'][contains(.,'Click for JS Alert')]"
        open_browser.get_url(url)
        open_browser.click_botton(locator_js)
        open_browser.alert_verify()
        alert = driver.switch_to.alert
        text = alert.text
        alert.accept()
        print(f"Alert:{text}, O alerta foi emitido com sucesso!")
    except:
        print('O alerta não foi exibido.')
    
if __name__ == "__main__":
    main()