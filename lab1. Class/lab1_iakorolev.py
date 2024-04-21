# Задание № 1

ff


class Car:
    brand = "VW"
    model = "Polo"

    def drive():
        print("Вперед!")


# Car.drive()

# Задание № 2


class Terminator:
    def say_greetings(self):
        print("I am T-700, give me your ride and jacket!")

    def say_goodbye(self):
        print("I'll be back!")


# T700 = Terminator()
# T800 = Terminator()

# T700.say_greetings()
# T700.say_goodbye()

# T800.say_greetings()
# T800.say_goodbye()

# Задание № 3


class Motorbike:

    def __init__(self, engine, year):
        self.engine = engine
        self.year = year

    def output(self):  # функция для теста класса
        return f"\nОбъем двигателя мотоцикла: {self.engine}\nГод выпуска мотоцикла: {self.year}"


# engine = input("Введите объем двигателя мотоцикла: ")
# year = input("Введите год выпуска мотоцикла: ")

# bike = Motorbike(engine, year)
# print(bike.output())

# Задание № 4


class Car:

    def __init__(self, br, mod, pr):
        self.brand = br
        self.model = mod
        self.price = price
        self.name = f"{br} {mod}"

    def __str__(self):
        return f"""\n{self.brand} - Бренд автомобиля\n{self.model} - Модель автомобиля\n{self.price} -
        Цена автомобиля\n{self.name} - Бренд и модель автомобиля
        """


# brand = input("Введите марку автомобиля: ")
# model = input("Введите модель автомобиля: ")
# price = input("Введите цену автомобиля: ")

# bmw = Car(brand, model, price)
# print(bmw)

# Задание № 5


class HockeyPlayer:

    def __init__(self, firs_name, last_name, goals=0, assist=0):
        self.first_name = firs_name
        self.last_name = last_name
        self.goals = goals
        self.assist = assist

    def add_goals(self):
        self.goals = int(self.goals) + 1

    def add_assist(self):
        self.assist = int(self.assist) + 1

    def statistics(self):
        return f"""\n{self.first_name} {self.last_name} - {float(self.goals) + 0.5*float(self.assist)}"""


# A,O = input("Введите имя хоккеиста: "), input("Введите фамилию хоккеиста: ")
# goals = input("Введите кол-во забитых шайб: ")
# assists = input("Введите кол-во передач: ")

# Aleksandr_Ovechkin = HockeyPlayer(A, O, goals, assists)

# print("До функции add_goals ", Aleksandr_Ovechkin.goals)

# Aleksandr_Ovechkin.add_goals()

# print("После add_goals ", Aleksandr_Ovechkin.goals)

# print(Aleksandr_Ovechkin.statistics())

# Задание № 6


class Array:
    values = 0

    def __init__(self, *args):
        self.args = []
        self.args = args
        self.values = self.get_integers()

    def get_integers(self):
        result = list(filter(lambda x: type(
            x) is int or type(x) is float, self.args))
        return sorted(result)

    def __str__(self):
        if self.values:
            return f"\nМассив{self.values}"
        else:
            return f"\nМассив пуст"


n = Array(1, 2, 3, 4, 6, "242", 31, "ke", 2.1, "saw", 2.124)
print(n)

empty = Array()
print(empty)
