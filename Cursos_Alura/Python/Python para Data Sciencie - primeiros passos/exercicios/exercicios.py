# ==========================
# BLOCO: COLETA E AMOSTRAGEM DE DADOS
# ==========================

# Desafio 1: Solicitar o nome e exibir saudação
# Resultado: Mostra o nome digitado pelo usuário.
nome = input('Digite seu nome: ')
print(f'Olá, {nome}.')

# Desafio 2: Solicitar nome e idade
# Resultado: Mostra nome e idade com formatação f-string.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'Olá {nome}, você tem {idade} anos.')

# Desafio 3: Solicitar nome, idade e altura
# Resultado: Exibe as informações formatadas em uma frase.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
print(f'Olá {nome}, você tem {idade} anos e mede {altura} metros!')


# ==========================
# BLOCO: CALCULADORA COM OPERADORES
# ==========================

# Desafio 1: Somar dois valores
# Resultado: Exibe a soma dos dois números.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a + b)

# Desafio 2: Somar três valores
# Resultado: Exibe a soma de três números inteiros.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print(a + b + c)

# Desafio 3: Subtração entre dois valores
# Resultado: Exibe o resultado da subtração.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a - b)

# Desafio 4: Multiplicação entre dois valores
# Resultado: Exibe o resultado da multiplicação.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a * b)

# Desafio 5: Divisão entre dois valores
# Resultado: Exibe o resultado da divisão (float).
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador / denominador)

# Desafio 6: Exponenciação
# Resultado: Exibe o resultado do operador elevado à potência.
operador = int(input('Digite o operador valor: '))
potencia = int(input('Digite a potência valor: '))
print(operador ** potencia)

# Desafio 7: Divisão inteira
# Resultado: Exibe o quociente inteiro da divisão.
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador // denominador)

# Desafio 8: Resto da divisão
# Resultado: Exibe o valor do resto da divisão.
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador % denominador)

# Desafio 9: Média aritmética de três notas
# Resultado: Exibe a média simples entre três valores.
nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
nota_3 = float(input('Digite a 3° nota: '))
print(f'Média {(nota_1 + nota_2 + nota_3) / 3}.')

# Desafio 10: Média ponderada
# Resultado: Exibe o resultado do cálculo da média ponderada.
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'Média {media_ponderada}.')


# ==========================
# BLOCO: EDITANDO TEXTOS
# ==========================

# Desafio 1: Exibir uma frase simples
# Resultado: Mostra a frase definida na variável.
frase = 'Olá Python!'
print(frase)

# Desafio 2: Coletar uma frase do usuário
# Resultado: Exibe a frase digitada.
frase = input('Digite uma frase: ')
print(frase)

# Desafio 3: Mostrar frase em maiúsculas
# Resultado: Converte e exibe toda a frase em letras maiúsculas.
frase = input('Digite uma frase: ')
print(frase.upper())

# Desafio 4: Mostrar frase em minúsculas
# Resultado: Converte e exibe toda a frase em letras minúsculas.
frase = input('Digite uma frase: ')
print(frase.lower())

# Desafio 5: Remover espaços no início e fim
# Resultado: Mostra a frase sem espaços extras.
frase = ' Olá Python!  '
print(frase.strip())

# Desafio 6: Remover espaços com input
# Resultado: Remove espaços extras digitados pelo usuário.
frase = input('Digite uma frase: ')
print(frase.strip())

# Desafio 7: Remover espaços e deixar minúsculo
# Resultado: Remove espaços e converte em minúsculas.
frase = input('Digite uma frase: ')
print(frase.strip().lower())

# Desafio 8: Substituir letras
# Resultado: Substitui 'e' por 'f' em uma frase minúscula.
frase = input('Digite uma frase: ')
print(frase.lower().replace('e', 'f'))

# Desafio 9: Substituir letra 'a' por '@' (Unicode 64)
# Resultado: Converte 'a' para '@'.
frase = input('Digite uma frase: ')
print(frase.lower().replace('a', chr(64)))

# Desafio 10: Substituir letra 's' por '$' (Unicode 36)
# Resultado: Converte 's' para '$'.
frase = input('Digite uma frase: ')
print(frase.lower().replace('s', chr(36)))
