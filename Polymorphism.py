class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

bird = Bird()
penguin = Penguin()
bird.fly()
penguin.fly()