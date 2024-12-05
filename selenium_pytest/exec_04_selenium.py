from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import pytest

class WebDriverConfig:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def open_url(self, url):
        self.webdriver.get(url)

    def preencher_campos(self, locator, name):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(name)

    def usar_select(self, select, select_pais):
        selecao = WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, select)))
        select_info = Select(selecao)
        select_info.select_by_visible_text(select_pais)

    def submit_botton(self, locator):
        WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).click()

    def verify_validation(self, locator):
        text_validation = WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        text_atual = text_validation.text
        text_esperado = "Thanks for contacting us, we will get back to you shortly."
        assert text_atual == text_esperado, f"O texto esperado é {text_esperado}, o texto retornado foi {text_atual}"
        
def main():
    driver = webdriver.Chrome()
    open_browser = WebDriverConfig(driver)
    lista_preencher = [{
        "Nome": "Patrick Carvalho",
        "Locator1": "//input[@id='name']",
        "Senha": "coxinha123",
        "Locator2": "//input[contains(@id,'inputPassword4')]",
        "Email": "patrick@hotmail.com",
        "Locator3": "//input[contains(@id,'inputEmail4')]",
        "Company": "55PBX",
        "Locator4": "//input[contains(@id,'company')]",
        "Website": "www.55pbx.com.br",
        "Locator5": "//input[contains(@id,'websitename')]",
        "Cidade": "São Paulo",
        "Locator6": "//input[contains(@id,'inputCity')]",
        "Endereço1": "Rua das pindamonhagabas",
        "Locator7": "//input[contains(@name,'address_line1')]",
        "Endereço2": "Rua das pindamonhagabonas",
        "Locator8": "//input[contains(@id,'inputAddress2')]",
        "Estado": "São Paulo",
        "Locator9": "//input[contains(@id,'inputState')]",
        "CEP": "04249080",
        "Locator10": "//input[contains(@id,'inputZip')]" 
    }]
    url = "https://www.lambdatest.com/selenium-playground/input-form-demo"
    open_browser.open_url(url)
    for preencher in lista_preencher:
        locator1 = preencher['Locator1']
        name  = preencher['Nome'] 
        open_browser.preencher_campos(locator1, name)
        locator2 = preencher['Locator2']
        senha = preencher['Senha']
        open_browser.preencher_campos(locator2, senha)
        locator3 = preencher['Locator3']
        email = preencher['Email']
        open_browser.preencher_campos(locator3, email)
        locator4 = preencher['Locator4']
        company = preencher['Company']
        open_browser.preencher_campos(locator4, company)
        locator5 = preencher['Locator5']
        website = preencher['Website']
        open_browser.preencher_campos(locator5, website)
        locator6 = preencher['Locator6']
        cidade = preencher['Cidade']
        open_browser.preencher_campos(locator6, cidade)
        locator7 = preencher['Locator7']
        Endereço1 = preencher['Endereço1']
        open_browser.preencher_campos(locator7, Endereço1)
        locator8 = preencher['Locator8']
        Endereço2 = preencher['Endereço2']
        open_browser.preencher_campos(locator8, Endereço2)
        locator9 = preencher['Locator9']
        estado = preencher['Estado']
        open_browser.preencher_campos(locator9, estado)
        locator10 = preencher['Locator10']
        estado = preencher['CEP']
        open_browser.preencher_campos(locator10, estado)
        
    select = "//select[@name='country']"
    pais = "Brazil"
    open_browser.usar_select(select, pais)
    salvar = "//button[@type='submit'][contains(.,'Submit')]"
    open_browser.submit_botton(salvar)
    sucess_text = "//p[@class='success-msg hidden'][contains(.,'Thanks for contacting us, we will get back to you shortly.')]"
    open_browser.verify_validation(sucess_text)
    time.sleep(5)



if __name__ == "__main__":
    main()