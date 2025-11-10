start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

print(f"Числа від {start} до {end}:")

for i in range(start, end + 1):
    print(i)