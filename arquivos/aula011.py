
# 1. (n + n) conta dentro dos parenteses
# 2. ** conta da potência
# 3. * / // % conta de multi, divi e seus derivados
# 4. + - conta de adição e multiplicação

conta = 1 + 1 ** 5 + 5  # 1 + 1^5 + 5 = 7
print(conta)

conta_1 = (1 + (0.5 + 0.5)) ** 5 + 5  # 1 + 1.0^5 + 5 = 37
print(conta_1)

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)  # 2^10 = 1024
print(conta_2)
