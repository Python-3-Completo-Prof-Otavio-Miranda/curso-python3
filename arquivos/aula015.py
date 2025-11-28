# Usando a função input para coletar dados do usuário

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# tentando corrigir de str para int mas não é recomendável
# numero_1 = int(input('Insira um número: '))
# numero_2 = int(input('Insira outro número: '))
# print(f'A soma dos números é: {numero_1 + numero_2}')

numero_1 = input('Insira um número: ')
numero_2 = input('Insira outro número: ')

# Forma correta neste momento do curso
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
