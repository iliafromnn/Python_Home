import random

class Card:
    def __init__(self, player_type):
        def sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBERS)
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBERS = 90
        self._MAX_NUMBERS_CARD = 15
        self._number_stroked = 0
        FREE_SPACE = 4
        NUMBERS_IN_LINE = 5

        self._numbers = random.sample(range(1, self._MAX_NUMBERS+1), self._MAX_NUMBERS_CARD)

        for line in self._card:
            for _ in range(FREE_SPACE):
                line.append(' ')
        for line in self._card:
            for _ in range(NUMBERS_IN_LINE):
                line.append(self._numbers.pop())

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
            else:
                return False

    def try_stroke(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._number_stroked += 1
                    if self._number_stroked >= self._MAX_NUMBERS_CARD:
                        raise Exception(f'{self.player_type} победил')
                    return True
            return False

    def __str__(self):
        MAX_FIELD = 3
        header = f'\n{self.player_type}:\n'
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD)
            body += '\n'
        return header + body

human_player = Card('Игрок')
computer_player = Card('Компьютер')

print(human_player)
print(computer_player)
