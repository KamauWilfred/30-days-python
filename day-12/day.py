class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def eat(self):
        print(f"{self.name} is eating dog food")
        
dog1 = Dog("Max", "Chihuahua")
print(vars(dog1))
dog1.eat()
