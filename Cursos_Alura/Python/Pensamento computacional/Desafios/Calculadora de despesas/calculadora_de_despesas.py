"""Calculadora de despesas.

O usuário informa uma despesa por vez. A soma continua até que ele digite 0,
quando o total acumulado é exibido. Não é necessário informar a quantidade
de despesas antecipadamente.
"""


def ler_valor(mensagem):
    """Lê um número do usuário, insistindo enquanto a entrada for inválida."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 45.90).")


def main():
    total = 0.0

    valor = ler_valor("Informe o valor da despesa (0 para encerrar): ")
    while valor != 0:
        total += valor
        valor = ler_valor("Informe o valor da despesa (0 para encerrar): ")

    print(f"Total gasto no mês: R$ {total:.2f}")


if __name__ == "__main__":
    main()
