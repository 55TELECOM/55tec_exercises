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
    
    def login_site(self, username_locator, username,senha_locator, senha, botao_login, verify_login):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, username_locator))).send_keys(username)
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, senha_locator))).send_keys(senha)
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, botao_login))).click()
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, verify_login)))
        except:
            print('Username ou senha incorreto!')

    def adicionar_carrinho(self, add_cart, verify_cart):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, add_cart))).click()
            WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, verify_cart)))
            print('O produto foi adicionado com sucesso ao carrinho!')
        except:
            print('O produto não foi adicionado ao carrinho.')



def main():
    driver = webdriver.Chrome()
    open_browser = WebDriverConfig(driver)
    driver.maximize_window()
    url = "https://www.saucedemo.com/"
    open_browser.get_url(url)
    username_locator = "//input[contains(@placeholder,'Username')]"
    username = "problem_user"
    senha_locator = "//input[contains(@id,'password')]"
    senha = "secret_sauce"
    botao_locator = "//input[contains(@id,'login-button')]"
    verify_login = "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Backpack')]"
    open_browser.login_site(username_locator, username, senha_locator, senha, botao_locator, verify_login)
    add_cart_locator = "//button[contains(@data-test,'add-to-cart-sauce-labs-backpack')]"
    verify_cart = "//a[@class='shopping_cart_link'][contains(.,'1')]"
    open_browser.adicionar_carrinho(add_cart_locator, verify_cart)
    time.sleep(2)
 

if __name__ == "__main__":
    main()