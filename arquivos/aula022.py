# Introdução aos Operadores Lógicos -> and (e) or(ou) not(não)

# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados 'falsy' (que vc já viu) 0 0.0 '' False
# Também existe o tipo 'None' que é usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito com and (e)
print(True and True and True)  # -> avalia se todos os valores são True
print(True and 0 and True)  # -> avalia e imprime o valor False
print()

# Avaliação de curto circuito com or (ou)
print(True or False)  # -> avalia o primeiro valor e já imprime True
print(True or False or 0)  # -> avalia o primeiro valor e já imprime True
print(0 or False or True)  # -> avalia o primeiro valor e já imprime True
print(0 or False or 'abc')  # -> avalia o primeiro valor e já imprime True
print(0 or False or 'abc' or True)  # -> mesmo resultado
print()

senha_1 = 0 or False or 0 or 'abc' or True
print(senha_1)

senha_2 = input('Senha: ') or 'Sem senha'
print(senha_2)
