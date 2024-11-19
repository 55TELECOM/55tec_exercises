# **Introdução**

Os exercícios apresentados têm uma progressão clara de complexidade e, em muitos casos, apresentam tarefas que se correlacionam entre si, como abrir páginas, interagir com elementos do DOM, preencher formulários e validar comportamentos. Dada essa natureza interconectada, é altamente recomendável adotar abordagens que promovam **boas práticas de desenvolvimento**, como o uso de **Programação Orientada a Objetos (POO)** ou **programação funcional**. 

Essas abordagens ajudam a estruturar o código de forma que ele seja mais **organizado**, **reutilizável** e **fácil de manter**, especialmente ao lidar com automações repetitivas ou testes complexos.

---

## **Por que considerar POO?**

1. **Organização e Clareza**: Com o uso de classes e métodos, você pode estruturar cada funcionalidade de forma modular. Por exemplo:
   - Uma classe `BrowserManager` pode gerenciar a configuração e inicialização do WebDriver.
   - Classes específicas como `LoginHandler` ou `FormHandler` podem encapsular interações comuns, como preencher campos ou clicar em botões.

   Exemplo básico:
   ```python
   class BrowserManager:
       def __init__(self, driver):
           self.driver = driver

       def open_url(self, url):
           self.driver.get(url)

       def find_element(self, locator):
           return self.driver.find_element(*locator)

   class LoginHandler(BrowserManager):
       def login(self, username, password):
           self.find_element(("id", "username")).send_keys(username)
           self.find_element(("id", "password")).send_keys(password)
           self.find_element(("id", "login-button")).click()
    ```

2. **Reutilização de Código**: Ao encapsular lógicas em classes ou métodos, você evita duplicação. Por exemplo, a lógica para inicializar o navegador ou preencher formulários pode ser reaproveitada em vários testes.

3. **Manutenção**: Com a POO, alterações ou melhorias podem ser feitas em um único lugar (na classe), sem necessidade de alterar todos os testes diretamente.

---

## **Por que considerar Programação Funcional?**

1. **Simplicidade em Fluxos**: Funções puras e pequenos blocos funcionais permitem criar pipelines claros de automação. Por exemplo:

    - Uma função para capturar dados da tabela pode ser reutilizada em qualquer contexto sem dependências de estado.
    - Funções como `login()` ou `fill_form()` podem ser escritas para aceitar argumentos dinâmicos e evitar acoplamento.
        Exemplo:
        ```python
        def open_page(driver, url):
            driver.get(url)

        def find_and_fill(driver, locator, value):
            driver.find_element(*locator).send_keys(value)

        def submit_form(driver, submit_locator):
            driver.find_element(*submit_locator).click()
        ```

2. **Modularidade**: A programação funcional incentiva a escrita de pequenas funções reutilizáveis, facilitando a manutenção e os testes unitários.

3. **Facilidade de Teste**: Funções puras (sem dependências externas) são mais fáceis de testar e simular, o que é uma grande vantagem ao trabalhar com Pytest.


# Questões

## **Nível 1: Automação Básica com Selenium**
### 1. Abrir um site e verificar o título
- Use Selenium para abrir o site `https://example.com`.
- Verifique se o título da página contém o texto "Example Domain".
- Use Pytest para escrever o teste e verificar o resultado.

---

## **Nível 2: Pesquisa em Campo de Entrada**
### 2. Automatizar uma pesquisa no Google
- Abra o site `https://www.google.com`.
- Digite "Python Selenium" no campo de pesquisa.
- Pressione Enter e verifique se a página de resultados contém links relevantes.

---

## **Nível 3: Navegação e Cliques**
### 3. Automação de navegação e clique
- Use Selenium para abrir o site `https://example.com`.
- Clique no link "More Information" (ou similar, dependendo do site).
- Verifique se a URL muda para a página esperada.

---

## **Nível 4: Preenchimento de Formulários**
### 4. Automação de formulário de contato
- Use Selenium para abrir o site https://www.lambdatest.com/selenium-playground/input-form-demo.
- Preencha os campos do formulário (nome, email, telefone, endereço, etc.).
- Clique no botão "Submit".
- Verifique se uma mensagem de validação ou sucesso é exibida após o envio do formulário.
---

## **Nível 5: Teste de Login**
### 5. Automatizar um fluxo de login
- Acesse o site `https://the-internet.herokuapp.com/login`.
- Insira um nome de usuário (`tomsmith`) e senha (`SuperSecretPassword!`).
- Clique no botão "Login".
- Verifique se a mensagem "You logged into a secure area!" aparece na página.

---

## **Nível 6: Manipulação de Popups e Alertas**
### 6. Interagir com alertas
- Acesse o site `https://the-internet.herokuapp.com/javascript_alerts`.
- Clique no botão "Click for JS Alert".
- Feche o alerta e verifique se a mensagem "You successfully clicked an alert" aparece na página.

---

## **Nível 7: Manipulação de DropDowns**
### 7. Selecionar opções em um dropdown
- Acesse o site https://www.lambdatest.com/selenium-playground/select-dropdown-demo.
- Escolha "Friday" no dropdown de dias da semana.
- Verifique se o texto "Day selected :- Friday" aparece abaixo do dropdown.
---

## **Nível 8: Manipulação de Tabelas**
### 8. Extrair dados de uma tabela
8. Extrair dados de uma tabela
- Acesse o site https://www.w3schools.com/html/html_tables.asp.
- Extraia os nomes das empresas na tabela "HTML Table Example".
- Salve os dados em um arquivo companies.txt, onde cada linha contém o nome de uma empresa.

---

## **Nível 9: Teste de Carrinho de Compras**
### 9. Automatizar fluxo de e-commerce
- Acesse o site https://www.saucedemo.com/.
- Faça login com as credenciais:
    - Usuário: standard_user
    - Senha: secret_sauce
- Adicione o primeiro item listado ao carrinho.
- Verifique se o carrinho mostra "1 item(s)".

---

## **Nível 10: Teste Paralelo com Pytest e Selenium**
### 10. Rodar testes em paralelo
- Crie dois testes:
    1. Verificar se o título da página https://example.com é "Example Domain".
    2. Click no texto "Click Here" na página https://the-internet.herokuapp.com/windows/ e verificar se foi aberto uma nova janela com sucesso.
- Use pytest-xdist para rodar os testes em paralelo.


