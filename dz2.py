class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.make} {self.model} {self.year}"

car1 = Car("Mitsubishi", "Lancer", 2008)
car2 = Car("Chevrolet", "Camaro", 2020)
car3 = Car("Audi", "R8", 2018)
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())