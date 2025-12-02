# Interpolação de strings (%) e a função len em Python #

"""
Interpolação básica de strings
s - string -> %s
d e i - int -> %d %i
f - float -> %f
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Magno'
preco = 1000.95897643
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (15, 15))
print('O hexadecimal de %d é %08x' % (1500, 1500))
print('O hexadecimal de %d é %04X' % (1500, 1500))
