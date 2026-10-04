import random


class Cat:
    def __init__(self, name="Cat"):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.cleanliness = 50

    def eat(self):
        self.hunger += 20
        self.happiness += 5
        print(f"{self.name} is eating")

    def sleep(self):
        self.energy += 30
        self.hunger -= 5
        print(f"{self.name} is sleeping")

    def play(self):
        self.happiness += 15
        self.energy -= 15
        self.hunger -= 5
        print(f"{self.name} is playing")

    def wash(self):
        self.cleanliness += 30
        self.happiness += 5
        print(f"{self.name} is washing")

    def days_indexes(self, day):
        day = f"Today is the {day} day of {self.name}'s life"
        print(f"{day:=^50}")
        print(f"Hunger - {self.hunger}")
        print(f"Happiness - {self.happiness}")
        print(f"Energy - {self.energy}")
        print(f"Cleanliness - {self.cleanliness}")
        print()

    def is_alive(self):
        if self.hunger <= 0:
            print(f"{self.name} is too hungry")
            return False

        if self.energy <= 0:
            print(f"{self.name} is too tired")
            return False

        if self.happiness <= 0:
            print(f"{self.name} is sad")
            return False

        return True

    def live(self, day):
        if self.is_alive() == False:
            return False

        self.days_indexes(day)

        dice = random.randint(1, 4)

        if self.hunger < 30:
            self.eat()
        elif self.energy < 30:
            self.sleep()
        elif self.happiness < 30:
            self.play()
        elif self.cleanliness < 30:
            self.wash()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.play()
        elif dice == 4:
            self.wash()


cat = Cat(name="Murchyk")

for day in range(1, 8):
    if cat.live(day) == False:
        break
