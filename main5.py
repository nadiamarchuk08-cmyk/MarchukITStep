n = int(input("Введіть число для обчислення факторіалу: "))
fac = 1
for i in range(1, n + 1):
    fac *= i

print(f"Факторіал числа {n} = {fac}")