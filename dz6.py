file_path = input("Введіть шлях до файлу: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        cont = file.read()
        print("Вміст файлу:")
        print(cont)
except FileNotFoundError:
    print("Помилка: файл за вказаним шляхом не існує.")
except Exception as error:
    print(f"Сталася інша помилка: {error}")