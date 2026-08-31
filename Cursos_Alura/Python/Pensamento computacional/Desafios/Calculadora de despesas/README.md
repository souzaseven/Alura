# Desafio: Calculadora de despesas

Sistema simples de controle financeiro pessoal. O usuário informa diversas
despesas do mês (mercado, transporte, lazer etc.) e, ao final, o sistema
apresenta o **total gasto**.

O usuário **não** informa quantas despesas tem. As entradas continuam até que
o valor digitado seja **zero** — nesse momento a soma total é exibida.

## Algoritmo em linguagem natural

1. Comece com o **total** igual a `0`.
2. Solicite ao usuário o **valor** de uma despesa.
3. Enquanto o **valor** informado for diferente de `0`:
   1. Some o **valor** ao **total**.
   2. Solicite o próximo **valor** de despesa.
4. Quando o **valor** informado for `0`, exiba o **total** acumulado.

### Por que funciona

- O `total` acumula cada despesa conforme ela é digitada.
- O laço "enquanto" se repete um número **indefinido** de vezes: não é preciso
  saber a quantidade de despesas antecipadamente.
- O valor `0` funciona como **sentinela** — a marca que encerra a repetição.
- Pedir o primeiro valor **antes** do laço garante que, se o usuário digitar `0`
  logo de cara, o total exibido seja `0` (nenhuma despesa registrada).

## Pseudocódigo (Portugol)

```
algoritmo "calculadora_de_despesas"
inicio
    real: total, valor

    total <- 0

    escreva("Informe o valor da despesa (0 para encerrar): ")
    leia(valor)

    enquanto (valor <> 0) faca
        total <- total + valor
        escreva("Informe o valor da despesa (0 para encerrar): ")
        leia(valor)
    fimenquanto

    escreva("Total gasto no mês: R$ ", total)
fimalgoritmo
```

## Fluxograma (descrição textual)

```
        ┌─────────────┐
        │   INÍCIO    │
        └──────┬──────┘
               ▼
        total = 0
               ▼
        ler valor
               ▼
        ┌─────────────┐   não (valor = 0)
        │ valor <> 0? ├───────────────┐
        └──────┬──────┘               ▼
               │ sim            escrever total
               ▼                      ▼
        total = total + valor   ┌─────────────┐
               ▼                │     FIM     │
        ler valor               └─────────────┘
               │
               └──► (volta ao teste "valor <> 0?")
```

## Implementação de referência (Python)

Veja [`calculadora_de_despesas.py`](calculadora_de_despesas.py).
