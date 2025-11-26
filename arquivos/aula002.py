# \r\n -> CRLF
# \N -> LF

print(12, 3, 34, 1011, sep="-", end='##')  # sep é o separador
print(56, 7, 78, 10, 11, sep='-')
print(9, 10, end='\n##')  # end significa final, pode quebrar a linha ou não
print(9, 10, end='##')  # end significa final, pode quebrar a linha ou não
