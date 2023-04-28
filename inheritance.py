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

class new_user(Person):
    """"Create class 'Job '"""
    def __init__(self, name, age, height, weight):
        """"initialisation of parent class attributes"""
        super().__init__(name, age, height, weight)
        self.job = " Programmer"

    def get_job(self):
        """"add job position"""
        print("Position is :" + str(self.job))

class new_user1(Person):
    """"Create class 'Job '"""
    def __init__(self, name, age, height, weight):
        """"initialisation of parent class attributes"""
        super().__init__(name, age, height, weight)
        self.job1 = " QA Engineer"

    def get_job1(self):
        """"add job position"""
        print("Position is :" + str(self.job1))

new_user = new_user("Danila", 22, 159, 64)
new_user.update_weight(68)
new_user.description_person()
new_user.get_job()
new_user1 = new_user1("Jenea" , 28 , 180 , 85)
new_user1.description_person()
new_user1.get_job1()
#
# man = Person("Anton", 22, 160, 60)
# women = Person ("Dasha" , 26 , 160 , 55)
# women1 = Person ("Dana" , 21 , 158 , 52)

