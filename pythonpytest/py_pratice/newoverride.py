from hashlib import new

from overrides import overrides


class Animal:
    def speak(self):
        pass
class Dog(Animal):
    overrides
    def speak(self):
        print("override")


class Cat(Animal):
    new
    def meow(self):
        print("meow")
dog = Dog()
dog.speak()  # Prints "Woof!"

cat = Cat()
cat.meow()