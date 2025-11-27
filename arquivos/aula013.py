nome = 'Magno V Gomes'
altura = 1.82
peso = 156
imc = peso / altura ** 2  # IMC = peso / (altura^2)

# f-strings - Formatação diferente da aula 12
resultado = f'Meu nome é {nome} tenho {altura:.2f} de altura, peso {peso} quilos e meu IMC é: {imc:.3f} \n'

print(resultado)
