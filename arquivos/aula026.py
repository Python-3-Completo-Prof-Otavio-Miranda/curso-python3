## Formatação básica de strings com 'f-strings' ##

"""
Formatação básica de strings
s - string -> %s
d - int -> %d
f - float -> %f

.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr__ __str__
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'-{variavel: ^10}-')
print(f'-{variavel:$^10}-')
print(f'-{variavel:0^10}-')

print(15 * '-')
print(f'{1000.4873648123746:.1f}')
print(f'{1000.4873648123746:,.1f}')
print(f'{1000.4873648123746:-,.1f}')
print(f'{1000.4873648123746:+,.1f}')

print(15 * '-')
print(f'{1000.4873648123746:0>+10,.1f}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'{1000.4873648123746:0=+10,.4f}')

print(15 * '-')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')

print(15 * '-')
print(f'{variavel!r}')
