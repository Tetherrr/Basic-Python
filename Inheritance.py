class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} : ARF")

class Eldest_Puppy(Dog):
    pass

class Youngest_Puppy(Dog):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def talk(self):
        print(f"{self.name}, {self.size}")

DogOne = Dog("Poe")
DogOne.sound()

PuppyOne = Eldest_Puppy("Poo")
PuppyOne.sound()

PuppyTwo = Youngest_Puppy("Pip", "Smallest")
PuppyTwo.talk()