class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")


class Dog(Animal):
    def speak(self):
        print(self.name, "says Woof")


class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow")


dog = Dog("Tommy")
cat = Cat("Kitty")

animals = [dog, cat]

for animal in animals:
    animal.speak()

