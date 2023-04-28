class Car():

    def __init__(self, model, year, engine, price, odo):
        """Инициализация атрибутов авто"""
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.odo = odo
        self.wheels = 4

    def description(self):
        """Вывод информации о автомобиле"""
        newline = '\n'
        print(f'Автомобиль: {self.model} {newline} Год выпуска: {self.year} {newline} Объем двигателя: {self.engine} л {newline} '
              f'Цена: {self.price} {newline} Пробег: {self.odo} км {newline} Колес: {self.wheels} {newline}' )

class Truck(Car):

    def __init__(self, model, year, engine, price, odo):
        """Инициализация атрибутов грузовика"""
        super().__init__(model, year, engine, price, odo)
        self.wheels = 8

    def description(self):
        """Вывод информации о грузовике"""
        newline = '\n'
        print(f'Автомобиль: {self.model} {newline} Год выпуска: {self.year} {newline} Объем двигателя: {self.engine} л {newline} '
              f'Цена: {self.price} {newline} Пробег: {self.odo} км {newline} Колес: {self.wheels} {newline}' )

NewCar = Car('Mazda', 2019, 2.0, 2500000, 4000)
NewCar.description()

NewTruck = Truck('Volvo', 2021, 6.3, 8500000, 80000)
NewTruck.description()