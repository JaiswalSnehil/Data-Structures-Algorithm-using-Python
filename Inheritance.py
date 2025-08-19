class Animal:
    def sound(self):
        return "some soumd"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"

# Example
dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())