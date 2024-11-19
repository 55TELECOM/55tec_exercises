# Nível 7: Comparação de Economia de Moedas
7. Comparação de Economia Global
- Use a API de Conversão de Moedas (https://exchangeratesapi.io/) para obter taxas de câmbio do USD para 5 moedas.
- Combine esses dados com a API do REST Countries (https://restcountries.com/) para calcular a renda per capita (em USD) de 10 países diferentes.
- Salve os dados no arquivo economia_global.csv no seguinte formato:
```sql
País,Moeda,Renda Per Capita (Local),Renda Per Capita (USD)
Brasil,BRL,45000,8571.43
Japão,JPY,4000000,36536.36
```