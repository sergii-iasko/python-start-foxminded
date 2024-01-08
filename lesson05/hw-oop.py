class MartialArts:

    def _punch(self):
        print("Punch")

    def _kick(self):
        print('Kick')

    def stance(self):
        pass

    def fight(self):
        self._punch()
        self._kick()
        self.stance()


class Wushu(MartialArts):
    country = 'China'

    def stance(self):
        print('Mabu')


class Karate(MartialArts):
    country = 'Japan'

    def stance(self):
        print('Kiba-Dachi')


def action(ma: MartialArts):
    ma.fight()

w = Wushu()
k = Karate()
action(w)
action(k)