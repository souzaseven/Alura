# Desafio: Calculando pedidos

Desafio do curso de **Pensamento Computacional** (Alura).

## Contexto

Funcionalidade de um aplicativo de lanchonete. O sistema calcula o **valor
total de um pedido** a partir da quantidade de cada item solicitado pelo
cliente.

## Regra de negócio

| Item          | Preço unitário |
|---------------|----------------|
| Hambúrguer    | R$ 12,00       |
| Batata frita  | R$ 7,00        |
| Refrigerante  | R$ 5,00        |

O valor total é a soma dos subtotais de cada item, onde
`subtotal = quantidade × preço unitário`.

## Algoritmo em linguagem natural

```
1. Início
2. Armazenar os preços fixos:
      preco_hamburguer = 12
      preco_batata     = 7
      preco_refri      = 5
3. Solicitar e ler as quantidades informadas pelo cliente:
      qtd_hamburguer, qtd_batata, qtd_refri
4. Calcular o subtotal de cada item:
      total_hamburguer = qtd_hamburguer * preco_hamburguer
      total_batata     = qtd_batata * preco_batata
      total_refri      = qtd_refri * preco_refri
5. Somar os subtotais:
      total_pedido = total_hamburguer + total_batata + total_refri
6. Exibir "Valor total do pedido: R$ " seguido de total_pedido
7. Fim
```

### Por que funciona

- Os **preços** ficam em variáveis próprias: se um valor mudar, basta ajustar
  um único ponto do algoritmo.
- As **quantidades** também vão para variáveis, separando o dado de entrada
  (o que o cliente pediu) do dado fixo (a tabela de preços).
- Cada **subtotal** é calculado de forma independente antes da soma, o que
  deixa o cálculo fácil de conferir item a item.
- O algoritmo é **linear**: não há decisão nem repetição — apenas
  entrada → cálculo → saída.
- Multiplicar por uma quantidade `0` resulta em subtotal `0`, então itens não
  pedidos simplesmente não afetam o total.

## Pseudocódigo (Portugol)

```
algoritmo "calculando_pedidos"
inicio
    real: preco_hamburguer, preco_batata, preco_refri
    inteiro: qtd_hamburguer, qtd_batata, qtd_refri
    real: total_hamburguer, total_batata, total_refri, total_pedido

    preco_hamburguer <- 12.00
    preco_batata     <- 7.00
    preco_refri      <- 5.00

    escreva("Quantidade de hambúrgueres: ")
    leia(qtd_hamburguer)
    escreva("Quantidade de batatas fritas: ")
    leia(qtd_batata)
    escreva("Quantidade de refrigerantes: ")
    leia(qtd_refri)

    total_hamburguer <- qtd_hamburguer * preco_hamburguer
    total_batata     <- qtd_batata * preco_batata
    total_refri      <- qtd_refri * preco_refri

    total_pedido <- total_hamburguer + total_batata + total_refri

    escreva("Valor total do pedido: R$ ", total_pedido)
fimalgoritmo
```

## Fluxograma (descrição textual)

```
        ┌─────────────┐
        │   INÍCIO    │
        └──────┬──────┘
               ▼
        preços fixos:
        preco_hamburguer = 12
        preco_batata     = 7
        preco_refri      = 5
               ▼
        ler qtd_hamburguer
        ler qtd_batata
        ler qtd_refri
               ▼
        total_hamburguer = qtd_hamburguer * preco_hamburguer
        total_batata     = qtd_batata     * preco_batata
        total_refri      = qtd_refri      * preco_refri
               ▼
        total_pedido = total_hamburguer + total_batata + total_refri
               ▼
        escrever total_pedido
               ▼
        ┌─────────────┐
        │     FIM     │
        └─────────────┘
```

## Teste de mesa

| qtd_hamburguer | qtd_batata | qtd_refri | total_hamburguer | total_batata | total_refri | total_pedido |
|:--------------:|:----------:|:---------:|:----------------:|:------------:|:-----------:|:------------:|
| 2              | 1          | 2         | R$ 24,00         | R$ 7,00      | R$ 10,00    | R$ 41,00     |
| 1              | 0          | 3         | R$ 12,00         | R$ 0,00      | R$ 15,00    | R$ 27,00     |
| 3              | 3          | 0         | R$ 36,00         | R$ 21,00     | R$ 0,00     | R$ 57,00     |
| 0              | 0          | 0         | R$ 0,00          | R$ 0,00      | R$ 0,00     | R$ 0,00      |

## Implementações

- [calcular_pedido.py](calcular_pedido.py) — versão em Python
- [calcular-pedido.js](calcular-pedido.js) — versão em JavaScript (Node.js)

### Como executar

```bash
python calcular_pedido.py
# ou
node calcular-pedido.js
```
