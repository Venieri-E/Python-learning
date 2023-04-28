class Person():
    """"Create person"""

    def __init__(self, name, age, height, weight):
        """"Initialization of human atribute"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description_person(self):
        """"Discription of person"""
        description = self.name + " Age: " + str(self.age) + "| Height(cm) = " + str(self.height) + " | Weight (kg) = " + str(self.weight)
        print("New user : " + description)

    def get_weight(self):
        print("Weight is :" + str(self.weight) + " kg")

    def get_height(self):
        print("Height is :" + str(self.height) + " cm")

    def get_age(self):
        print("Age is :" + str(self.age))

    def get_name(self):
        print("His/She's name is :" + self.name)

    def update_weight(self , kg):
        """"Change weight"""
        self.weight = kg

# man = Person ("Jenea" , 28 , 180 , 85)
women = Person ("Dasha" , 26 , 160 , 55)
# man.description_person()
# man.get_weight()
# man.get_height()
# man.get_age()
# man.get_name()
women.description_person()
# women.get_weight()
# women.get_height()
# women.get_age()
# women.get_name()
women.update_weight(58)
women.get_weight()
