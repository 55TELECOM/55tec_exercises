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

    def plataform_login(self,locator, username, locator_senha, senha, locator_login):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(username)
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator_senha))).send_keys(senha)
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator_login))).click()

    def verify_login(self, locator_login, locator_login_first):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator_login)))
            print("O login foi realizado com sucesso!")
        except:
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator_login_first)))
            print("O login falhou! Verifique seu username e senha.")

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    open_browser = WebDriverConfig(driver)
    url = "https://the-internet.herokuapp.com/login"
    open_browser.get_url(url)
    username = "tomsmith"
    username_locator = "//input[contains(@id,'username')]"
    senha = "SuperSecretPassword!"
    locator_senha = "//input[contains(@id,'password')]"
    login_locator = "//i[@class='fa fa-2x fa-sign-in'][contains(.,'Login')]"
    verify_locator = "//div[contains(@class,'flash success')]"
    verify_locator_first = "//div[contains(@class,'flash error')]"
    open_browser.plataform_login(username_locator, username, locator_senha, senha, login_locator)
    open_browser.verify_login(verify_locator, verify_locator_first)
    

    time.sleep(2)

    

if __name__ == "__main__":
    main()