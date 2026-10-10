class Dog:
    def speak(self):
        print("dog woof!")

class Cat:
    def speak(self):
        print("cat meeows!")

animals =[Dog(), Cat()]
for animal in animals:
    animal.speak()
