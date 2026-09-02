# Desafio: Calculando o valor da entrega

## Descrição do problema

Uma empresa de delivery cobra a taxa de entrega de acordo com a distância
até o cliente e com a ocorrência de chuva no momento do pedido.

Regras:

| Distância            | Taxa base |
|----------------------|-----------|
| Até 5 km             | R$ 5,00   |
| Mais de 5 e até 10 km| R$ 8,00   |
| Acima de 10 km       | R$ 10,00  |

- Se estiver chovendo, acrescentar **R$ 2,00** à taxa base.

## Algoritmo em linguagem natural

### 1. Entrada

1. Solicitar ao usuário a **distância** até o endereço do cliente, em quilômetros.
2. Perguntar se **está chovendo**, aceitando uma resposta booleana (verdadeiro ou falso).

### 2. Processamento

3. Definir a **taxa base** de acordo com a distância informada:
   - Se a distância for menor ou igual a 5 km, a taxa base é R$ 5,00.
   - Senão, se a distância for menor ou igual a 10 km, a taxa base é R$ 8,00.
   - Senão (distância maior que 10 km), a taxa base é R$ 10,00.
4. Definir o **adicional de chuva**:
   - Se estiver chovendo, o adicional é R$ 2,00.
   - Senão, o adicional é R$ 0,00.
5. Calcular o **valor final** da entrega:
   - valor final = taxa base + adicional de chuva.

### 3. Saída

6. Exibir uma mensagem clara com o valor total, por exemplo:
   `Taxa de entrega: R$ 10,00`

## Pseudocódigo

```
INÍCIO
    LEIA distancia            // em km
    LEIA estaChovendo         // verdadeiro ou falso

    SE distancia <= 5 ENTÃO
        taxaBase <- 5.00
    SENÃO SE distancia <= 10 ENTÃO
        taxaBase <- 8.00
    SENÃO
        taxaBase <- 10.00
    FIM SE

    SE estaChovendo ENTÃO
        adicional <- 2.00
    SENÃO
        adicional <- 0.00
    FIM SE

    valorFinal <- taxaBase + adicional

    ESCREVA "Taxa de entrega: R$ ", valorFinal
FIM
```

## Testes de mesa

| Distância | Chuva | Taxa base | Adicional | Valor final |
|-----------|-------|-----------|-----------|-------------|
| 3 km      | não   | R$ 5,00   | R$ 0,00   | **R$ 5,00** |
| 5 km      | sim   | R$ 5,00   | R$ 2,00   | **R$ 7,00** |
| 8 km      | não   | R$ 8,00   | R$ 0,00   | **R$ 8,00** |
| 10 km     | sim   | R$ 8,00   | R$ 2,00   | **R$ 10,00**|
| 15 km     | não   | R$ 10,00  | R$ 0,00   | **R$ 10,00**|
| 12 km     | sim   | R$ 10,00  | R$ 2,00   | **R$ 12,00**|

> Observação sobre os limites: o enunciado diz "até 5 km" e "acima de 10 km".
> Os valores exatos de 5 km e 10 km foram considerados dentro da faixa de
> menor valor (5 km → R$ 5,00; 10 km → R$ 8,00), usando os operadores `<=`.
