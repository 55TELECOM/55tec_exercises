# Nível 6: Detecção de Anomalias
6. Detecção de Anomalias Climáticas
    - Use a API do OpenWeatherMap (https://openweathermap.org/api) para buscar os dados climáticos de 20 cidades nos últimos 15 dias.
    - Identifique dias com variações de temperatura superiores a 10 graus em relação à média das temperaturas diárias.
    - Salve os dados no arquivo anomalies.csv no seguinte formato:
    ```
    Cidade,Data,Temperatura,Variação
    São Paulo,2024-11-01,18.0,-12.0
    Nova York,2024-11-03,32.0,+14.0
    ```