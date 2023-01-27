class Transport:

    def __init__(self, wheels, speed):
        self.__wheels = wheels
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels):
        self.__speed = wheels

    def __str__(self):
        return f'Кількість колес = {self.__wheels}\nМакс. швидкість - {self.__speed} км\год'


class Auto(Transport):
    def __init__(self, wheels, speed, number, hp):
        super().__init__(wheels, speed)
        self.__number = number
        self.__hp = hp

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def wheels(self, hp):
        self.__hp = hp

    def __str__(self):
        return (f'Державгний номер - {self.__number}\n'
                f'Потужність двигуна - {self.__hp} к\с\n{super().__str__()}')


class Bus(Auto):
    def __init__(self, wheels, speed, number, hp, passengers):
        super().__init__(wheels, speed, number, hp)
        self.__passengers = passengers

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def number(self, passengers):
        self.__passengers = passengers

    def __str__(self):
        return (f'Кількість пасажирів {self.passengers}\n{super().__str__()}')


class Truck(Auto):

    def __init__(self, wheels, speed, number, hp, tonnage):
        super().__init__(wheels, speed, number, hp)
        self.__tonnage = tonnage

    @property
    def tonnage(self):
        return self.__tonnage

    @tonnage.setter
    def tonnage(self, tonnage):
        self.__tonnage = tonnage

    def __str__(self):
        return (f'Тонаж - {self.__tonnage} тон\n{super().__str__()}')


class Bicycle(Transport):

    def __init__(self, wheels, speed, weight):
        super().__init__(wheels, speed)
        self.__weight = weight

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def __str__(self):
        return (f'Вага - {self.__weight} кг.\n{super().__str__()}')


class Motorbike(Bicycle):
    def __init__(self, wheels, speed, weight, volume):
        super().__init__(wheels, speed, weight)
        self.__volume = volume

    @property
    def volume(self):
        return self.volume

    @volume.setter
    def weight(self, volume):
        self.__volume = volume

    def __str__(self):
        return (f'Потужність двигуна- {self.__volume} квт\n{super().__str__()}')


# bus = Transport(2, 4)
# bicycle = Bicycle(1, 2, 3, 5)
# print(bicycle)
bus = Motorbike(1, 2, 3,5)
print(bus)
