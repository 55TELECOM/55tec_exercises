# Exercício 4: Pares Divisíveis pela Soma

## Objetivo
Dado um array de números inteiros e um número inteiro positivo `k`, determine o número de pares `(i, j)` onde:
- `i < j`
- `(ar[i] + ar[j])` é divisível por `k`.

---

## Descrição da Função
Complete a função `divisibleSumPairs` que deve:
- Receber como entrada o tamanho do array `n`, o divisor `k`, e o array `ar`.
- Retornar o número de pares válidos `(i, j)`.

---

## Entrada
1. Um número inteiro `n` (tamanho do array) e outro inteiro `k` (divisor), separados por espaço.
2. Uma linha com `n` números inteiros representando os elementos do array `ar`.

---

## Saída
- Retorne um único número inteiro representando o número de pares válidos.

---

## Restrições
- `2 <= n <= 100`
- `1 <= k <= 100`
- `1 <= ar[i] <= 100`

---

## Exemplo de Entrada
```plaintext
6 3
1 3 2 6 1 2
```

## Exemplo de Saída
```plaintext
5
```

---

## Explicação
Dado o array ar = [1, 3, 2, 6, 1, 2] e k = 3:

Pares Válidos:
- (0, 2) → ar[0] + ar[2] = 1 + 2 = 3 (divisível por 3)
- (0, 5) → ar[0] + ar[5] = 1 + 2 = 3 (divisível por 3)
- (1, 3) → ar[1] + ar[3] = 3 + 6 = 9 (divisível por 3)
- (2, 4) → ar[2] + ar[4] = 2 + 1 = 3 (divisível por 3)
- (4, 5) → ar[4] + ar[5] = 1 + 2 = 3 (divisível por 3)

Total de pares válidos: 5.

