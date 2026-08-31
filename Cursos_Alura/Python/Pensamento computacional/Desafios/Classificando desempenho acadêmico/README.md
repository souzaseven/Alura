# Classificando desempenho acadêmico

Desafio do curso de **Pensamento Computacional** (Alura).

## Contexto

Sistema educacional que exibe uma mensagem personalizada para cada estudante
com base na sua média final.

## Regra de negócio

| Faixa da média         | Mensagem exibida                 |
|------------------------|----------------------------------|
| Menor que 5,0          | `Você está reprovado.`           |
| De 5,0 até 6,9         | `Você está de recuperação.`      |
| 7,0 ou mais            | `Parabéns! Você foi aprovado.`   |

## Algoritmo em linguagem natural

```
1. Início
2. Solicitar a média final do estudante.
3. Ler e armazenar o valor informado na variável "media".
4. Se "media" for menor que 5,0:
      4.1. Exibir "Você está reprovado."
   Senão, se "media" for menor que 7,0:
      4.2. Exibir "Você está de recuperação."
   Senão:
      4.3. Exibir "Parabéns! Você foi aprovado."
5. Fim
```

### Por que a estrutura encadeada funciona

- As condições `se / senão se / senão` são avaliadas em ordem: cada teste só
  acontece se o anterior deu falso. Isso garante que **apenas uma** mensagem
  seja exibida.
- No segundo teste não é preciso escrever `media >= 5,0 e media <= 6,9`, porque
  ao chegar ali o algoritmo já sabe que a média **não** é menor que 5,0. Basta
  verificar se é menor que 7,0.
- O `senão` final cobre todos os casos restantes (média igual ou acima de 7,0).

## Teste de mesa

| Média informada | 1º teste (`< 5,0`) | 2º teste (`< 7,0`) | Mensagem exibida             |
|-----------------|--------------------|--------------------|------------------------------|
| 4,0             | Verdadeiro         | —                  | Você está reprovado.         |
| 5,0             | Falso              | Verdadeiro         | Você está de recuperação.    |
| 6,9             | Falso              | Verdadeiro         | Você está de recuperação.    |
| 7,0             | Falso              | Falso              | Parabéns! Você foi aprovado. |
| 9,5             | Falso              | Falso              | Parabéns! Você foi aprovado. |

## Implementações

- [classificar_desempenho.py](classificar_desempenho.py) — versão em Python
- [classificar-desempenho.js](classificar-desempenho.js) — versão em JavaScript (Node.js)

### Como executar

```bash
python classificar_desempenho.py
# ou
node classificar-desempenho.js
```
