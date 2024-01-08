class Dog:
    legs_num: int = 4

    def __init__(self, age=4, name='Rex'):
        self.age = age
        self.name = name

    def __repr__(self):
        return 'Dog(age={}, name={})'.format(self.age, self.name)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        self.age == other.age

    def say_gav(self):
        print(self.age)

d1 = Dog(age = 5)
d2 = Dog(age = 6)

print(d1<d2)