# Exercício 8: Happy Ladybugs

## Objetivo
Dado um tabuleiro com joaninhas representado por uma string, determine se é possível rearranjar as joaninhas para que todas fiquem "felizes".  
Uma joaninha é feliz quando suas células adjacentes (esquerda ou direita) contêm outra joaninha da mesma cor.

---

## Descrição da Função
Complete a função `happyLadybugs` que deve:
- Receber como entrada uma string `b` representando o tabuleiro.
- Retornar "YES" se todas as joaninhas podem ser rearranjadas para ficarem felizes, ou "NO" caso contrário.

---

## Regras
1. O tabuleiro é representado por uma string:
   - Cada caractere pode ser uma letra maiúscula (`A-Z`) indicando a cor de uma joaninha, ou `_` indicando uma célula vazia.
2. Uma joaninha é feliz se suas células adjacentes (esquerda ou direita) têm outra joaninha da mesma cor.
3. Você pode mover joaninhas para células vazias (`_`).

---

## Entrada
1. Um número inteiro `g`, representando o número de jogos.
2. Para cada jogo:
   - Um número inteiro `n`, o número de células no tabuleiro.
   - Uma string `b`, de tamanho `n`, representando o tabuleiro.

---

## Saída
- Retorne "YES" se todas as joaninhas podem ser rearranjadas para ficarem felizes, ou "NO" caso contrário.

---

## Restrições
- `1 ≤ g ≤ 100`
- `1 ≤ n ≤ 10^5`

---

## Exemplo de Entrada 1
```plaintext
4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR
```

## Exemplo de Saída 1
```plaintext
YES
NO
YES
YES
```

--

## Explicação
### Caso 1:
Tabuleiro inicial: RBY_YBR

- Podemos rearranjar as joaninhas para RRBBYY_ para que todas fiquem felizes.
- Retorne YES.

### Caso 2:
Tabuleiro inicial: X_Y__X

- Não há espaço suficiente para mover as joaninhas X para ficarem juntas.
- Retorne NO.

### Caso 3:
Tabuleiro inicial: __

- Não há joaninhas infelizes.
- Retorne YES.

### Caso 4:
Tabuleiro inicial: B_RRBR

- Podemos mover a joaninha B para que o tabuleiro fique RRBBRR.
- Retorne YES.
