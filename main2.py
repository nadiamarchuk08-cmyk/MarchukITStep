import random

number = random.randint(1, 10)
attempts = 3

print("Вгадайте число від 1 до 10. У вас є 3 спроби.")

for i in range(attempts):
    guess = int(input("Введіть число: "))

    if guess == number:
        print("Ви вгадали число!")
        break
    elif guess < number:
        print("Більше")
    else:
        print("Менше")
else:
    print(f"Спроби закінчилися. Загадане число було {number}.")