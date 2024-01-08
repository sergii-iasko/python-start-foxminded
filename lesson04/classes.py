class Dog:
    legs_num: int = 4

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def say_your_age(self):
        print(self.age)

    def say_your_name(self):
        print(self.name)

dog1 = Dog(age = 4, name = 'John')
dog1.say_your_age()
dog1.say_your_name()
print(dog1.legs_num)

dog2 = Dog(age = 8, name = 'Rex')
dog2.say_your_age()
dog2.say_your_name()
dog2.legs_num = 5
print(dog2.legs_num)