class Person():
    """"Human Model"""

    def __init__( self , name, age):
        """"Initialization of human atribute - name , age"""
        self.name = name
        self.age = age
        print("Human succes created")

    def talk(self):
        """"ask the man to talk"""
        print(self.name + " Talking")

    def sing(self):
        """"ask the man to sing"""
        print(self.name + " Singing")

man = Person("Jenea" , 28)
women = Person("Daria" , 26)
# print(man.name)
women.sing()
man.talk()
