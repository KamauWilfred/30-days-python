class Car:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"{self.brand} {self.model} {self.year}")
car1 = Car("Mercedes","GLE", 2020)
car2 = Car("Toyota", "Harrier", 2023)
print(vars(car1))
car1.info()
car2.info()


