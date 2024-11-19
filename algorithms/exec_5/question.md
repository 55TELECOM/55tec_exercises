# Exercício 5: Identificação do Tipo de Pássaro Mais Comum

## Objetivo
Dado um array representando avistamentos de pássaros, onde cada elemento é o ID de um tipo de pássaro, determine o ID do tipo mais frequentemente avistado.  
Se houver mais de um tipo com a mesma frequência máxima, retorne o menor ID.

---

## Descrição da Função
Complete a função `migratoryBirds` que deve:
- Receber como entrada um array de números inteiros representando os tipos de pássaros avistados.
- Retornar o menor ID do tipo de pássaro mais frequentemente avistado.

---

## Entrada
1. O primeiro valor de entrada é um inteiro `n`, que indica o tamanho do array `arr`.
2. O segundo valor de entrada é o array `arr` com `n` números inteiros, onde cada número é o ID do tipo de pássaro.

---

## Saída
- Retorne o menor ID do tipo de pássaro mais frequentemente avistado.

---

## Restrições
- Cada tipo de pássaro é garantido como um dos seguintes: `1`, `2`, `3`, `4`, `5`.

---

## Exemplo de Entrada 1
```plaintext
6
1 4 4 4 5 3
```

## Exemplo de Saída 1
```plaintext
4
```

## Explicação
Os diferentes tipos de pássaros ocorrem com as seguintes frequências:

- Tipo 1: 1 avistamento
- Tipo 4: 3 avistamentos
- Tipo 5: 1 avistamento
- Tipo 3: 1 avistamento

O tipo com maior frequência é o 4, com 3 avistamentos. Resultado: 4.

---

## Exemplo de Entrada 2
```plaintext
11
1 2 3 4 5 4 3 2 1 3 4
```

## Exemplo de Saída 2
```plaintext
3
```

## Explicação
Os diferentes tipos de pássaros ocorrem com as seguintes frequências:

- Tipo 1: 2 avistamentos
- Tipo 2: 2 avistamentos
- Tipo 3: 3 avistamentos
- Tipo 4: 3 avistamentos
- Tipo 5: 1 avistamento

Os tipos 3 e 4 têm a mesma frequência máxima de 3. Retornamos o menor ID: 3.

