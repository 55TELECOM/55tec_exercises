# Exercício 2: Diferença Absoluta das Diagonais de uma Matriz

## Objetivo
Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de suas diagonais.

---

## Descrição da Função
Complete a função `diagonalDifference` que deve:
- Receber como entrada uma matriz quadrada de números inteiros.
- Retornar a diferença absoluta entre a soma da diagonal principal e da diagonal secundária.

---

## Entrada
1. O primeiro valor de entrada é um número inteiro, `n`, que indica o número de linhas e colunas da matriz.
2. Os próximos `n` valores representam as linhas da matriz, com números inteiros separados por espaço.

---

## Saída
- Retorne a diferença absoluta entre as somas das duas diagonais como um único número inteiro.

---

## Restrições
- A matriz sempre será quadrada, ou seja, terá o mesmo número de linhas e colunas.

---

## Exemplo de Entrada
```plaintext
3
11 2 4
4 5 6
10 8 -12
```

## Exemplo de Saída
```plaintext
15
```

---


## Explicação
A matriz dada é:
```plaintext
11  2   4
 4  5   6
10  8 -12
```

### Diagonal Principal (da esquerda para a direita):
- Elementos: 11, 5, -12
- Soma: 11 + 5 - 12 = 4

### Diagonal Secundária (da direita para a esquerda):
- Elementos: 4, 5, 10
- Soma: 4 + 5 + 10 = 19

### Diferença Absoluta:
- |Soma da Diagonal Principal - Soma da Diagonal Secundária| = |4 - 19| = 15

