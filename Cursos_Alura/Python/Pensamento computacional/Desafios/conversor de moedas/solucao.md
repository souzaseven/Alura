# Desafio: Conversor de Moedas

Sistema de apoio para uma agência de viagens. O usuário informa um valor em
reais (R$) e o sistema mostra quanto isso representa em dólares (US$),
usando uma taxa de câmbio definida pela empresa.

---

## Algoritmo em linguagem natural

### Função de conversão

```
FUNÇÃO converter_para_dolar(valor_em_reais, taxa_de_cambio)
    valor_convertido <- valor_em_reais / taxa_de_cambio
    RETORNE valor_convertido
FIM FUNÇÃO
```

**Entrada da função:**
- `valor_em_reais`: quantia em reais que se deseja converter
- `taxa_de_cambio`: quantos reais valem 1 dólar (ex.: 5.20)

**Saída da função:**
- `valor_convertido`: a quantia equivalente em dólares

### Programa principal

```
INÍCIO
    ESCREVA "Informe o valor em reais (R$): "
    LEIA valor_em_reais

    ESCREVA "Informe a taxa de câmbio atual (R$ por US$ 1): "
    LEIA taxa_de_cambio

    dolar <- converter_para_dolar(valor_em_reais, taxa_de_cambio)

    ESCREVA "Com a taxa atual, o valor em dólares é: US$ ", dolar
FIM
```

---

## Passo a passo do raciocínio

1. **Decompor o problema:** separar o cálculo da conversão (regra de negócio)
   da interação com o usuário (entrada e saída).
2. **Criar uma função reutilizável** `converter_para_dolar` que recebe o valor
   em reais e a taxa de câmbio como parâmetros e devolve o valor em dólares.
3. **Aplicar a fórmula:** `valor_convertido = valor_em_reais / taxa_de_cambio`.
   Divide-se porque a taxa representa quantos reais custam 1 dólar.
4. **No programa principal:** pedir os dois dados ao usuário, chamar a função
   e exibir o resultado com uma mensagem clara.

---

## Exemplo de execução

```
Informe o valor em reais (R$): 1000
Informe a taxa de câmbio atual (R$ por US$ 1): 5.00
Com a taxa atual, o valor em dólares é: US$ 200.00
```

Cálculo: `1000 / 5.00 = 200`

---

## Por que usar uma função

- **Reutilização:** o mesmo cálculo pode ser chamado várias vezes no programa.
- **Organização:** o programa principal fica focado no fluxo, sem misturar a
  regra de cálculo.
- **Manutenção:** para adicionar outras moedas (euro, libra) ou ajustar a
  fórmula, basta alterar a função, sem mexer no resto do código.
