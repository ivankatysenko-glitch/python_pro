import random


class Human:

    def __init__(self, name):
        self.name = name
        self.age = 0  # Вік у роках
        self.health = 100  # Здоров'я (від 0 до 100)
        self.happiness = 70  # Щастя (не нижче 40%)
        self.money = 0  # Баланс
        self.alive = True

        # Вік природної смерті від старості (75-95 років)
        self.max_age = random.randint(75, 95)

    def get_older(self):
        self.age += 1
        if self.age < 30:
            aging_loss = 1
        elif self.age < 60:
            aging_loss = 2
        else:
            aging_loss = 4

        # Здоров'я зменшується, але не падає нижче 0
        self.health = max(0, self.health - aging_loss)

    def update_happiness(self, change):
        """Щастя тримається строго в межах від 40% до 100%"""
        self.happiness += change
        if self.happiness < 40:
            self.happiness = 40
        elif self.happiness > 100:
            self.happiness = 100

    def random_life_event(self):
        if self.age < 7:
            events = [
                ("гуляє в парку з батьками, все чудово", 10, 0),
                ("трохи підхопив застуду та сумує вдома", -12, 0),
                ("грається з улюбленими іграшками", 8, 0),
                ("капризує через погану погоду", -8, 0)
            ]
        elif 7 <= self.age < 18:
            events = [
                ("втомився від навчання та складних іспитів", -15, 0),
                ("весело провів час із шкільними друзями", 15, 0),
                ("посварився через дрібниці з однокласниками", -10, 0),
                ("отримав гарну оцінку за важливий проєкт", 12, 0),
                ("просто нудьгує вдома на вихідних", -6, 0)
            ]
        elif 18 <= self.age < 65:
            events = [
                ("отримав хорошу премію на роботі", 15, 1200),
                ("мав важкий робочий місяць та відчув втому", -15, 400),
                ("чудово відпочив із друзями на пікніку", 18, -200),
                ("зламалася побутова техніка, довелося ремонтувати", -12, -300),
                ("просто провів спокійний вечір за переглядом фільму", 5, 0),
                ("рік видався напруженим через робочі справи", -14, 200)
            ]
        else:
            events = [
                ("сумує за минулими часами та старою роботою", -10, 0),
                ("з радістю зустрівся з рідними та близькими", 20, 0),
                ("почувається трохи втомленим від негоди", -8, 0),
                ("спокійно доглядає за домашнім садом", 10, 0)
            ]

        description, happy_change, money_change = random.choice(events)

        if money_change < 0 and self.money < abs(money_change):
            print(f"{self.name} хотів(-ла) відпочити, але бракує коштів, тому залишається вдома.")
            self.update_happiness(-5)
        else:
            print(f"{self.name} {description}.")
            self.update_happiness(happy_change)
            self.money += money_change

    def visit_doctor(self):
        if self.money >= 300:
            print(f"🏥 {self.name} проходить плановий огляд у лікаря.")
            self.health = min(100, self.health + 3)
            self.money -= 300
        else:
            print(f"⚠️ У {self.name} недостатньо грошей на візит до лікаря.")
            self.update_happiness(-5)

    def check_alive(self):
        """Миттєва перевірка: якщо здоров'я <= 0 або досягнуто граничного віку"""
        if self.health <= 0:
            print(f"\n💥 {self.name} пішов(-ла) з життя через критичне погіршення здоров'я у віці {self.age} років.")
            self.alive = False
        elif self.age >= self.max_age:
            print(
                f"\n✨ {self.name} прожив(-ла) довге й насичене життя і спокійно помер(-ла) від старості у віці {self.age} років.")
            self.alive = False

    def end_of_year(self):
        print(f"Статус -> Вік: {self.age} | Здоров'я: {self.health} | Щастя: {self.happiness}% | Гроші: ${self.money}")

    def live_year(self):
        year_title = f" Вік {self.age} для {self.name} "
        print(f"{year_title:=^50}")

        # 1. Початок року та дорослішання
        self.get_older()

        # Одразу перевіряємо, чи живий персонаж після старіння
        self.check_alive()
        if not self.alive:
            return

        # 2. Подія протягом року
        self.random_life_event()

        # 3. Візит до лікаря
        if self.age > 40 and random.random() < 0.3:
            self.visit_doctor()

        self.end_of_year()
        self.check_alive()
        print()


# Запуск симуляції
person = Human(name="Alex")

while person.alive:
    person.live_year()