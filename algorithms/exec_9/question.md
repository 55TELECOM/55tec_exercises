# Exercício 9: Subconjunto Não Divisível

## Objetivo
Dado um conjunto de números inteiros distintos, determine o tamanho do maior subconjunto no qual a soma de quaisquer dois números não é divisível por um dado número \(k\).

---

## Descrição da Função
Complete a função `nonDivisibleSubset` que deve:
- Receber como entrada:
  - Um número inteiro \(k\): o divisor.
  - Um array \(S\): os números do conjunto.
- Retornar um inteiro representando o tamanho máximo do subconjunto.

---

## Entrada
1. A primeira linha contém dois inteiros \(n\) e \(k\), representando o número de elementos no conjunto \(S\) e o divisor.
2. A segunda linha contém \(n\) números inteiros distintos, separados por espaço.

---

## Saída
- Retorne um único número inteiro representando o tamanho do maior subconjunto.

---

## Restrições
- Todos os números no conjunto são distintos.

---

## Exemplo de Entrada 1
```plaintext
STDIN    Function
-----    --------
4 3      S[] size n = 4, k = 3
1 7 2 4  S = [1, 7, 2, 4]
```

## Exemplo de Saída 1
```plaintext
3
```

---

## Explicação
O conjunto S=[1,7,2,4].
Testando todos os subconjuntos possíveis:

```
1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6
```

- Subconjunto [1,7,4]: as somas 1+7=8, 1+4=5, 7+4=11 não são divisíveis por 3.
- Tamanho do subconjunto: 3.