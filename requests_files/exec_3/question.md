# Nível 3: Análise de Sentimentos em Postagens
3. Análise de Sentimentos e Classificação de Posts
    - Use a API do JSONPlaceholder (https://jsonplaceholder.typicode.com/) para:
        1. Buscar todos os posts de todos os usuários.
        2. Para cada post, analise o sentimento do título (positivo, negativo ou neutro) usando uma biblioteca de análise de texto, como TextBlob (https://textblob.readthedocs.io/en/dev/).
        3. Classifique os posts de acordo com os sentimentos e identifique os usuários que publicaram mais posts positivos.
    - Salve os dados no arquivo analise_sentimentos_posts.csv no seguinte formato:
    ```arduino
    Usuário,Título,Sentimento
    João,"Hoje é um ótimo dia",Positivo
    Maria,"Eu odeio segundas-feiras",Negativo
    ```