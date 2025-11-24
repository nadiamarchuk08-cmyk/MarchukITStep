class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} увімкнено.")
        else:
            print(f"{self.name} вже увімкнено.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} вимкнено.")
        else:
            print(f"{self.name} вже вимкнено.")

class Phone(Device):
    def call(self, number):
        if self.is_on:
            print(f"Телефон дзвонить на номер {number}...")
        else:
            print("Телефон вимкнений. Неможливо зробити дзвінок.")


class Laptop(Device):
    def open_program(self, program):
        if self.is_on:
            print(f"Відкриваю програму: {program}")
        else:
            print("Ноутбук вимкнено. Неможливо відкрити програму.")


class TV(Device):
    def change_channel(self, channel):
        if self.is_on:
            print(f"Перемикаю на канал {channel}")
        else:
            print("Телевізор вимкнений. Неможливо перемкнути канал.")

phone = Phone("Iphone 13")
laptop = Laptop("Acer Nitro 5")
tv = TV("Samsung QLED")

phone.turn_on()
laptop.turn_on()
tv.turn_off()

phone.call("123-456")
laptop.open_program("Chrome")
tv.change_channel(5)

tv.turn_on()
tv.change_channel(5)