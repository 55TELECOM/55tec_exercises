# Exercício 3: Conversão de Hora para Formato Militar (24 horas)

## Objetivo
Dada uma hora no formato de 12 horas AM/PM, converta-a para o formato de 24 horas (militar).

---

## Descrição da Função
Complete a função `timeConversion` que deve:
- Receber como entrada uma string representando uma hora no formato de 12 horas (AM/PM).
- Retornar uma string representando a mesma hora no formato de 24 horas.

---

## Regras:
- `12:00:00AM` no formato de 12 horas é equivalente a `00:00:00` no formato de 24 horas.
- `12:00:00PM` no formato de 12 horas é equivalente a `12:00:00` no formato de 24 horas.
- Para outras horas:
  - Adicione 12 ao horário da manhã (AM) para convertê-lo ao formato de 24 horas.
  - A hora do período da tarde (PM) já está no formato correto, exceto para `12PM`.

---

## Entrada
- Uma única string `s` no formato de 12 horas (AM/PM), como `07:05:45PM`.

---

## Saída
- Retorne uma string no formato de 24 horas (militar).

---

## Restrições
- Todas as entradas são válidas e seguem o formato de 12 horas (AM/PM).

---

## Exemplo de Entrada
```plaintext
07:05:45PM
```

## Exemplo de Saída
```plaintext
19:05:45
```

---

## Explicação
### Exemplo 1:
Entrada: 07:05:45PM

- A hora é 07 no formato PM.
- No formato de 24 horas, somamos 12 ao horário para obter 19.
- Resultado: 19:05:45.

### Exemplo 2:
Entrada: 12:01:00AM

- A hora é 12 no formato AM, que corresponde a 00 no formato de 24 horas.
- Resultado: 00:01:00.
