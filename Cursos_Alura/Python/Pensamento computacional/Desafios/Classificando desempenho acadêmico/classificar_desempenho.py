"""
Classificando desempenho acadêmico
Desafio do curso de Pensamento Computacional (Alura).

Recebe a média final do estudante e exibe uma mensagem de acordo
com a regra pedagógica, usando estruturas condicionais encadeadas.
"""


def classificar(media):
    """Retorna a mensagem correspondente à média informada."""
    if media < 5.0:
        return "Você está reprovado."
    elif media < 7.0:
        return "Você está de recuperação."
    else:
        return "Parabéns! Você foi aprovado."


def ler_media():
    """Solicita a média ao usuário, aceitando vírgula ou ponto decimal."""
    while True:
        entrada = input("Informe a média final do estudante (0 a 10): ")
        try:
            media = float(entrada.replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número, por exemplo: 7,5")
            continue

        if media < 0 or media > 10:
            print("Média inválida. Informe um valor entre 0 e 10.")
            continue

        return media


def main():
    media = ler_media()
    print(classificar(media))


if __name__ == "__main__":
    main()
