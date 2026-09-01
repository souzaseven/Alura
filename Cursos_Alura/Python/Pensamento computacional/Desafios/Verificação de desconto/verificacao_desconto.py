"""Desafio Alura - Pensamento computacional: Verificação de desconto (meia-entrada).

Regra: o cliente tem direito à meia-entrada se tiver menos de 18 anos OU for estudante.
"""


def tem_direito_meia_entrada(idade: int, estudante: bool) -> bool:
    """Retorna True se o cliente tem direito à meia-entrada."""
    return idade < 18 or estudante


def mensagem_desconto(idade: int, estudante: bool) -> str:
    """Retorna a mensagem correspondente à situação do cliente."""
    if tem_direito_meia_entrada(idade, estudante):
        return "Meia-entrada aplicada."
    return "Valor integral."


def ler_booleano(pergunta: str) -> bool:
    """Lê uma resposta do tipo sim/não (ou V/F) e converte para booleano."""
    resposta = input(pergunta).strip().lower()
    return resposta in ("s", "sim", "v", "verdadeiro", "true", "1")


def main() -> None:
    idade = int(input("Informe a idade do cliente: "))
    estudante = ler_booleano("O cliente é estudante? (s/n): ")
    print(mensagem_desconto(idade, estudante))


if __name__ == "__main__":
    main()
