import sys

class Player:
    def __init__(self, pos):
        self._pos = pos
        self._score = 0

    def move(self, steps):
        pos = self._pos + (steps % 10)
        self._pos = ((pos - 1) % 10) + 1
        self._score += self._pos

    def get_score(self):
        return self._score

    def __str__(self):
        return f"pos={self._pos}, score={self._score}"

class Dice:
    def __init__(self):
        self._value = 1
        self._rolls = 0

    def roll(self):
        value = self._value
        self._value += 1
        if self._value > 100:
            self._value = 1
        self._rolls += 1
        return value

    def get_rolls(self):
        return self._rolls

players = []
with open(sys.argv[1]) as f:
    players.append(Player(int(f.readline().strip().split(': ')[1])))
    players.append(Player(int(f.readline().strip().split(': ')[1])))


def do_round(dice, players):
    for player in players:
        player.move(dice.roll() + dice.roll() + dice.roll())
        if player.get_score() >= 1000:
            return False
    return True

def print_scores(dice, players):
    for player in players:
        print(f"player={player}, calc={player.get_score()*dice.get_rolls()}")

dice = Dice()
while do_round(dice, players):
    pass

print_scores(dice, players)
