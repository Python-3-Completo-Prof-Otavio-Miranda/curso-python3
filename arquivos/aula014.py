# Formatação de strings com o método format (f)
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string = 'a= {} -> b= {} c= {}'  # sem índices
formato = string.format(a, b, c)
print(formato)

string = 'a= {0} -> b= {1} c= {2:.2f}'  # com índices
formato = string.format(a, b, c)
print(formato)


# exemplos abaixo serão com parâmetros nomeados
# e no mesmo código as variáveis mudam de valor, algo não recomendado
a = 'Magno'
b = 'Neusa'
c = 'Vão casar'

string = 'a= {nome1} b= {nome2} c= {nome3}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
