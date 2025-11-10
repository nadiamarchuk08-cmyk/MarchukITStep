a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
sign = input("Вкажіть дію (+, -, *, /): ")

if sign == '+':
    print(f"Результат: {a + b}")
elif sign == '-':
    print(f"Результат: {a - b}")
elif sign == '*':
    print(f"Результат: {a * b}")
elif sign == '/':
    if b == 0:
        print("Помилка: ділення на нуль!")
    else:
        print(f"Результат: {a / b}")
else:
    print("Введіть лише +, -, *, /")