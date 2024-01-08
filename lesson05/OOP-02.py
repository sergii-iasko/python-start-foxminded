from abc import ABC, abstractmethod


class Animal(ABC):

    def eat(self):
        print('Eating...')

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print('GAV GAV')


class Cat(Animal):

    def sound(self):
        print('Mhew...')


def some_function(animal: Animal):
    print('do smth..')
    animal.sound()


some_function(Cat())