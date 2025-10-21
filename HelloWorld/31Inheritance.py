class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
# write pass if no function in it


class Cat(Mammal):
    def meow(self):
        print("meow")


dog = Dog()
dog.walk()
dog.bark()
cat = Cat()
cat.walk()
cat.meow()

