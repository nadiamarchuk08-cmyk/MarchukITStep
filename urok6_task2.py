number = input("Введіть число: ")
try:
    number_float = float(number)
    number_int = int(number_float)
    print("Результат:", number_int)
except ValueError:
    print("Введені дані не можна конвертувати в число")