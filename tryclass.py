class Cars():
    """"Create car"""

    def __init__(self, model, year, capacity, price, milleage, wheels):
        """"Initialization of car atribute"""
        self.model = model
        self.year = year
        self.capacity = capacity
        self.price = price
        self.milleage = milleage
        self.wheels = wheels

    def description_car(self):
        """"Discription of car"""
        result_1 = str(self.model) + " Year " + str(self.year) + "| Capacity = " + str(self.capacity) + " |Price = " + str(self.price) + "| Milleage = " + str(self.milleage) + " Qty of Wheels :" + str(self.wheels)
        print("New car : " + result_1)


car_1 =Cars("BMW", 1995, 2, 5000, 313456, 4)
car_1.description_car()


class new_truck_1(Cars):
    """"Create class 'Job '"""
    def __init__(self, model, year, capacity, price, milleage, wheels):
        """"initialisation of parent class attributes"""
        super().__init__(self, model, year, capacity, price, milleage, wheels)
        self.job1 = " QA Engineer""

    def get_job1(self):
        """"add job position"""
        print("Position is :" + str(self.job1))

new_truck_1 = ("Mann", 2002, 12, 76883, 98343, 8)
new_truck_1