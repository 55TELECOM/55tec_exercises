# Nível 1: Análise Avançada de Usuários e Tarefas
1. Agregação Avançada de Dados de Tarefas
    - Use a API do JSONPlaceholder (https://jsonplaceholder.typicode.com/) para:
        1. Obter todos os usuários.
        2. Para cada usuário, listar todas as tarefas associadas a ele, separando entre concluídas (completed = true) e não concluídas (completed = false).
    - Calcule a porcentagem de tarefas concluídas por cada usuário e identifique o usuário mais produtivo.
    - Salve os dados no arquivo analise_tarefas_avancada.csv no seguinte formato:
    ```graphql
    Nome,Email,Tarefas Concluídas,Tarefas Não Concluídas,Porcentagem Concluída,Produtividade
    João,joao@email.com,10,5,66.67,Não
    Maria,maria@email.com,20,0,100.00,Sim
    ```