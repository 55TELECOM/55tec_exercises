from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
 
class WebdriverConfig:
    def __init__(self, webdriver):
        self.webdriver = webdriver
    
    def open_url(self, url):
        self.webdriver.get(url)
        
    def verify_title(self):
        titulo_atual = self.webdriver.title
        WebDriverWait(self.webdriver, 10).until(EC.title_is((titulo_atual)))
        titulo_esperado = "Example Domain"
        assert titulo_esperado == titulo_atual, f"O título esperado era {titulo_esperado}, mas o encontrado foi {titulo_atual}."
        
def main():
    driver = webdriver.Chrome()
    open_browser = WebdriverConfig(driver)
    open_browser.open_url("https://example.com/")
    open_browser.verify_title()
    driver.quit()

    
if __name__ == "__main__":

    main()


#def click_element(self, locator):
        #return WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).click()
#open_browser.click_element("//a[contains(.,'More information...')]")