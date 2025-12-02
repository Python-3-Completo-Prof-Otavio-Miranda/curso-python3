# Introdução aos Operadores Lógicos
# and (e) or(ou) not(não) in (entre) e not in (não entre)

# Operadores in e not in
# Strings são iteráveis = navegar item por item

#  0 1 2 3 4 5 6 7 8 9 10
#  M a g n o V G o m e s
# -11-10-9-8-7-6-5-4-3-2-1

# nome = 'Magno'
# print(nome[2])
# print(nome[-4])
# print(10 * '-')  # -> dez traços para separar valores

# print('g' in nome)  # -> letra 'g' está nome? True
# print('H' in nome)  # -> letra 'H' está nome? False
# print(10 * '-')

# print('gno' in nome)  # -> letras 'gno' está nome? True
# print('zero' in nome)  # -> nome 'zero' está nome? False

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
