class Building:

    def __init__(self, name, height, width, length):
        self.name = name
        self.height = height
        self.width = width
        self.length = length

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{} (name={}, height={})'.format(self.__class__.__name__, self.name, self.height)

    def __lt__(self, other):
        return self.height * self.width * self.length < other.height * other.width * other.length

    def __gt__(self, other):
        return self.height * self.width * self.length > other.height * other.width * other.length


b1 = Building('Tower', 4, 6, 8)
b2 = Building('Loft', 4, 5, 5)
print(b1 < b2)
