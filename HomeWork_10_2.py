from abc import ABC, abstractmethod

class Wear:
    def __init__(self, type_size):
        self.size = type_size

    @abstractmethod
    def consuption(self):
        pass

class Coat(Wear):

    @property
    def consuption(self):
        return round((self.size / 6.5) + 0.5)

class Suit(Wear):

    @property
    def consuption(self):
        return round((self.size * 2) + 0.3)

coat = Coat(50)
suit = Suit(180)

print(coat.consuption)
print(suit.consuption)