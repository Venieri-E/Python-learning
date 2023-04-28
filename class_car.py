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


class new_truck_1(Cars):
    """"Create class 'Truck' '"""
    def __init__(self, model, year, capacity, price, milleage, wheels):
         """"initialisation of parent class attributes"""
         super().__init__(model, year, capacity, price, milleage, wheels)
         self.new_car_2 = "since 2005"


    def get_new_truck1(self):
        """"add truck position"""
        print("Old model " + str(self.new_car_2))


class new_truck2(Cars):
    """"Create class 'Truck' '"""
    def __init__(self, model, year, capacity, price, milleage, wheels):
        """"initialisation of parent class attributes"""
        super().__init__(model, year, capacity, price, milleage, wheels)
        self.new_car_2 = "Bought this year"

    def get_new_truck2(self):
        """"add truck position"""
        print("New car in park, " + str(self.new_car_2))


car_1 =Cars("BMW", 1995, 2, 5000, 313456, 4)
car_1.description_car()

new_truck_1 = new_truck_1("Mann", 2002, 12, 76883, 98343, 8)
new_truck_1.description_car()
new_truck_1.get_new_truck1()

new_truck2 = new_truck2("DAF", 2005, 16, 1000000, 182343, 8)
new_truck2.description_car()
new_truck2.get_new_truck2()

