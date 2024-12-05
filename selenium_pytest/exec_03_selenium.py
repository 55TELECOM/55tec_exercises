from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class WebDriverConfig:
    def __init__(self,webdriver):
        self.webdriver = webdriver
        
    def open_url(self, url):
        self.webdriver.get(url)
        url_atual = self.webdriver.current_url
        assert url_atual == url, f"A url esperada é {url_atual}, a retornada foi {url}"

    def click_element(self, locator):
        url_anterior = self.webdriver.current_url
        WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, locator))).click()
        url_esperada = self.webdriver.current_url
        assert url_anterior != url_esperada, "As Url não se alteraram"
        print(f'URL anterior: {url_anterior}, URL atual: {url_esperada}')

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    open_browser = WebDriverConfig(driver)
    url_atual = "https://example.com/"
    open_browser.open_url(url_atual)
    click_locator = "//a[@href='https://www.iana.org/domains/example'][contains(.,'More information...')]"
    open_browser.click_element(click_locator)
    time.sleep(2)
    

if __name__ == "__main__":
    main()