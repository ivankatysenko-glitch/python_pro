import random


class Human:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.happiness = 70
        self.money = 0
        self.alive = True

        self.max_age = random.randint(75, 95)

    def get_older(self):
        self.age += 1
        if self.age < 30:
            aging_loss = 1
        elif self.age < 60:
            aging_loss = 2
        else:
            aging_loss = 4


        self.health = max(0, self.health - aging_loss)

    def update_happiness(self, change):
        """Happiness stays strictly within the range of 40% to 100%"""
        self.happiness += change
        if self.happiness < 40:
            self.happiness = 40
        elif self.happiness > 100:
            self.happiness = 100

    def random_life_event(self):
        if self.age < 7:
            events = [
                ("is walking in the park with parents, everything is great", 10, 0),
                ("caught a slight cold and is feeling sad at home", -12, 0),
                ("is playing with favorite toys", 8, 0),
                ("is throwing a tantrum due to bad weather", -8, 0)
            ]
        elif 7 <= self.age < 18:
            events = [
                ("is tired from studying and difficult exams", -15, 0),
                ("had a fun time with school friends", 15, 0),
                ("argued over trifles with classmates", -10, 0),
                ("got a good grade on an important project", 12, 0),
                ("is simply bored at home on the weekend", -6, 0)
            ]
        elif 18 <= self.age < 65:
            events = [
                ("got a nice bonus at work", 15, 1200),
                ("had a hard working month and felt tired", -15, 400),
                ("had a great rest with friends on a picnic", 18, -200),
                ("home appliances broke down, had to repair them", -12, -300),
                ("simply spent a quiet evening watching a movie", 5, 0),
                ("the year turned out to be tense due to work matters", -14, 200)
            ]
        else:
            events = [
                ("misses past times and old work", -10, 0),
                ("happily met with relatives and loved ones", 20, 0),
                ("feels a bit tired from the bad weather", -8, 0),
                ("is quietly tending to the home garden", 10, 0)
            ]

        description, happy_change, money_change = random.choice(events)

        if money_change < 0 and self.money < abs(money_change):
            print(f"{self.name} wanted to relax, but lacks funds, so stays at home.")
            self.update_happiness(-5)
        else:
            print(f"{self.name} {description}.")
            self.update_happiness(happy_change)
            self.money += money_change

    def visit_doctor(self):
        if self.money >= 300:
            print(f"🏥 {self.name} is undergoing a routine check-up with a doctor.")
            self.health = min(100, self.health + 3)
            self.money -= 300
        else:
            print(f"⚠️ {self.name} doesn't have enough money for a doctor's visit.")
            self.update_happiness(-5)

    def check_alive(self):
        """Instant check: if health <= 0 or age limit is reached"""
        if self.health <= 0:
            print(f"\n💥 {self.name} passed away due to critical health deterioration at the age of {self.age}.")
            self.alive = False
        elif self.age >= self.max_age:
            print(
                f"\n✨ {self.name} lived a long and fulfilling life and peacefully passed away from old age at the age of {self.age}.")
            self.alive = False

    def end_of_year(self):
        print(
            f"Status -> Age: {self.age} | Health: {self.health} | Happiness: {self.happiness}% | Money: ${self.money}")

    def live_year(self):
        year_title = f" Age {self.age} for {self.name} "
        print(f"{year_title:=^50}")


        self.get_older()

        self.check_alive()
        if not self.alive:
            return

        self.random_life_event()

        # 3. Doctor visit
        if self.age > 40 and random.random() < 0.3:
            self.visit_doctor()

        self.end_of_year()
        self.check_alive()
        print()


person = Human(name="Alex")

while person.alive:
    person.live_year()