n = int(input("Введіть число n: "))

print(f"Парні числа від {n} до 1:")

for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i)