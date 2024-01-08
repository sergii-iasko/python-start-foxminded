class Dog:

    def __init__(self, age=4, name='Rex'):
        self.age = age
        self.name = name
        self._heart = 'Big heart'

    def _open_mouth(self):
        print('opening...')

    def _give_sound(self):
        print('GAV GAV')

    def _close_mouth(self):
        print("closing...")

    def say_gav(self):
        self._open_mouth()
        self._give_sound()
        self._close_mouth()


d = Dog()

d.say_gav()