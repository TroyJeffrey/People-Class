# Troy Jeffrey Amegashie
# 11/ 14/ 2019
# People Class

import random

class Person():

    def __init__(self, first, last, age, height, number):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.height = height
        self.fav_number = number

    def description(self):
        print(f"The name of this person is "
              f"{self.first_name} {self.last_name}."
              f"Their age is {self.age} and they are {self.height} inches tall.")

    def birthday(self):
        self.age = self.age + 1
        print(f"This person is now {self.age}.")

    def favorite_number(self):
        self.fav_number = random.randint(1,11)
        print(f"Their favorite number is {self.fav_number}.")


person1 = Person("George", "Jeremy", 25, 75, ())

person1.description()
person1.birthday()
person1.favorite_number()
