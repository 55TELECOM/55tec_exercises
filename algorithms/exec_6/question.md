# Exercício 6: O Dia do Programador

## Objetivo
Determinar a data do "Dia do Programador" (o 256º dia do ano) para um dado ano no intervalo entre 1700 e 2700, considerando as mudanças no calendário da Rússia ao longo da história.

---

## Descrição da Função
Complete a função `dayOfProgrammer` que deve:
- Receber como entrada um inteiro representando o ano.
- Retornar uma string no formato `dd.mm.yyyy`, representando a data do 256º dia do ano.

---

## Regras:
1. De 1700 a 1917, a Rússia usou o **calendário juliano**:
   - Um ano é bissexto se for divisível por 4.
2. A partir de 1919, a Rússia passou a usar o **calendário gregoriano**:
   - Um ano é bissexto se for divisível por 400, ou se for divisível por 4 mas **não divisível por 100**.
3. O ano de 1918 foi o ano da transição:
   - O dia 14 de fevereiro foi o 32º dia do ano (fevereiro teve 15 dias a menos).

---

## Entrada
- Um único número inteiro `year`, representando o ano.

---

## Saída
- Retorne uma string no formato `dd.mm.yyyy` representando o 256º dia do ano.

---

## Restrições
- `1700 ≤ year ≤ 2700`

---

## Exemplo de Entrada 1
```plaintext
2017
```

## Exemplo de Saída 1
```plaintext
13.09.2017
```

## Explicação
- O ano de 2017 é não bissexto no calendário gregoriano.
- Os primeiros 8 meses somam 243 dias.
- O 256º dia está no dia 256 - 243 = 13 de setembro.

---

## Exemplo de Entrada 2
```plaintext
2016
```

## Exemplo de Saída 2
```plaintext
12.09.2016
```

## Explicação
- O ano de 2016 é bissexto no calendário gregoriano.
- Os primeiros 8 meses somam 244 dias.
- O 256º dia está no dia 256 - 244 = 12 de setembro.

---

## Exemplo de Entrada 3
```plaintext
1800
```

## Exemplo de Saída 3
```plaintext
12.09.1800
```

## Explicação
- O ano de 1800 é bissexto no calendário juliano.
- Os primeiros 8 meses somam 244 dias.
- O 256º dia está no dia 256 - 244 = 12 de setembro.
