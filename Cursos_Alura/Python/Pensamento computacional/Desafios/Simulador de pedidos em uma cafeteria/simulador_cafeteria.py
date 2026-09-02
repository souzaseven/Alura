"""
Desafio: Simulador de pedidos em uma cafeteria

O sistema registra os pedidos de um cliente, calcula o valor total e,
caso o cliente seja cadastrado, aplica um desconto de 10% sobre o total.
"""

# --- Entrada ---
quantidade_itens = int(input("Quantos itens o cliente vai pedir? "))

total = 0

for numero_item in range(1, quantidade_itens + 1):
    nome_item = input(f"Nome do item {numero_item}: ")
    preco_item = float(input(f"Preço do item '{nome_item}': R$ "))
    total += preco_item

# --- Processamento ---
resposta_cadastro = input("O cliente é cadastrado? (S/N): ").strip().upper()
cliente_cadastrado = resposta_cadastro == "S"

if cliente_cadastrado:
    desconto = total * 0.10
    total_final = total - desconto
else:
    desconto = 0
    total_final = total

# --- Saída ---
print("\n----- Resumo do Pedido -----")
print(f"Valor total: R$ {total:.2f}")

if cliente_cadastrado:
    print(f"Desconto (10%): R$ {desconto:.2f}")
    print(f"Valor final com desconto: R$ {total_final:.2f}")
else:
    print(f"Valor final (sem desconto): R$ {total_final:.2f}")
