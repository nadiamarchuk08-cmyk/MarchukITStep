score = int(input("Введіть кількість балів від 0 до 100): "))

if 0 <= score <= 49:
    print("Незадовільно")
elif 50 <= score <= 69:
    print("Задовільно")
elif 70 <= score <= 89:
    print("Добре")
elif 90 <= score <= 100:
    print("Відмінно")
else:
    print("Кількість балів має бути від 0 до 100.")