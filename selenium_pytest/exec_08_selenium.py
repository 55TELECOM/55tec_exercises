from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import json
import requests
import pandas as pd
import pytest
import time

class WebDriverConfig:
    def __init__(self, webdriver):
        self.webdriver = webdriver
       
    def get_url(self, url):
        self.webdriver.get(url)
    
    def tabela(self, tabela_locator):
        return WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, tabela_locator))).text

    def arquivo_txt(self, lista_companys):
        with open('Companies.txt', 'w') as arquivo:
            for company in lista_companys:
                arquivo.write(str(company) + '\n') 

def main():
    driver = webdriver.Chrome()
    open_browser = WebDriverConfig(driver)
    url = "https://www.w3schools.com/html/html_tables.asp"
    open_browser.get_url(url)
    lista_company = ("//td[contains(.,'Alfreds Futterkiste')]", "//td[contains(.,'Centro comercial Moctezuma')]", "//td[contains(.,'Ernst Handel')]", "//td[contains(.,'Island Trading')]", "//td[contains(.,'Laughing Bacchus Winecellars')]", "//td[contains(.,'Magazzini Alimentari Riuniti')]")
    lista_company_complete = []
    for lista in lista_company:
        lista_full = open_browser.tabela(lista)
        lista_company_complete.append({
            "Compania": lista_full,
        })

    open_browser.arquivo_txt(lista_company_complete)
    


if __name__ == "__main__":
    main()