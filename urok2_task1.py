from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, "%d.%m.%Y")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def get_info(self):
        status = "Виконано" if self.completed else "Не виконано"
        return (f"Назва: {self.title}\n"
                f"Опис: {self.description}\n"
                f"Дедлайн: {self.deadline.strftime('%d.%m.%Y')}\n"
                f"Статус: {status}\n")

    def str(self):
        status = "Виконано" if self.completed else "Невиконано"
        return f"{status} {self.title} — до {self.deadline.strftime('%d.%m.%Y')}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано.\n")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.\n")
                return
        print(f"Завдання '{title}' не знайдено.\n")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Завдання '{title}' позначено як виконане.\n")
                return
        print(f"Завдання '{title}' не знайдено.\n")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.\n")
        else:
            print("Список завдань:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.title}")
            print()

    def show_task_details(self, title):
        for task in self.tasks:
            if task.title == title:
                print("Деталі завдання:\n")
                print(task.get_info())
                return
        print(f"️Завдання '{title}' не знайдено.\n")

if __name__ == "__main__":
    manager = TaskManager()
    task1 = Task("Курсова робота", "Написати перші два пункти", "20.11.2025")
    task2 = Task("Купити продукти", "Молоко, хліб, сир", "11.11.2025")

    manager.add_task(task1)
    manager.add_task(task2)

    manager.show_tasks()

    manager.show_task_details(task1.title)

    manager.mark_task_completed(task2.title)

    manager.remove_task(task2.title)

    manager.show_tasks()