"""Calculando pedidos.

Calcula o valor total de um pedido de lanchonete a partir das quantidades
de hambúrgueres, batatas fritas e refrigerantes informadas pelo cliente.
Desafio do curso de Pensamento Computacional (Alura).
"""

PRECO_HAMBURGUER = 12.00
PRECO_BATATA = 7.00
PRECO_REFRI = 5.00


def ler_quantidade(mensagem):
    """Lê uma quantidade inteira e não negativa, insistindo se a entrada for inválida."""
    while True:
        try:
            quantidade = int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro (ex.: 2).")
            continue

        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
            continue

        return quantidade


def calcular_total(qtd_hamburguer, qtd_batata, qtd_refri):
    """Retorna o valor total do pedido somando o subtotal de cada item."""
    total_hamburguer = qtd_hamburguer * PRECO_HAMBURGUER
    total_batata = qtd_batata * PRECO_BATATA
    total_refri = qtd_refri * PRECO_REFRI
    return total_hamburguer + total_batata + total_refri


def main():
    qtd_hamburguer = ler_quantidade("Quantidade de hambúrgueres: ")
    qtd_batata = ler_quantidade("Quantidade de batatas fritas: ")
    qtd_refri = ler_quantidade("Quantidade de refrigerantes: ")

    total_pedido = calcular_total(qtd_hamburguer, qtd_batata, qtd_refri)

    print(f"Valor total do pedido: R$ {total_pedido:.2f}")


if __name__ == "__main__":
    main()
