# Nível 8: Relatório de Filmes com Avaliação
8. Ranking Avançado de Filmes
    - Use a API do TMDb (https://developer.themoviedb.org/docs/getting-started) para buscar os filmes mais populares e suas avaliações.
    - Para cada filme, calcule o desvio padrão das avaliações (se a API fornecer isso) e ordene os filmes por menor variabilidade.
    - Salve os dados no arquivo ranking_filmes.csv no seguinte formato:
    ```mathematica
    Filme,Nota Média,Número de Avaliações,Desvio Padrão
    O Senhor dos Anéis,8.9,15000,0.5
    Matrix,8.7,12000,0.7
    ```