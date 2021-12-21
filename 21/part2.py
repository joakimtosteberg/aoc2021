import copy
import sys

class Player:
    def __init__(self, pos, name):
        self._name = name
        self._pos = pos-1
        self._score = 0

    def move(self, steps):
        pos = self._pos + (steps % 10)
        self._pos = ((pos - 1) % 10) + 1
        self._score += self._pos

    def get_score(self):
        return self._score

    def __str__(self):
        return f"pos={self._pos}, score={self._score}"

players = []
with open(sys.argv[1]) as f:
    players.append(Player(int(f.readline().strip().split(': ')[1]), "p1"))
    players.append(Player(int(f.readline().strip().split(': ')[1]), "p2"))

step_counts = {}
for roll1 in range(1,4):
    for roll2 in range(1,4):
        for roll3 in range(1,4):
            roll_value = roll1 + roll2 + roll3
            step_counts[roll_value] = step_counts.get(roll_value,0) + 1

        
def do_rounds(win_counts, step_counts, c_p_pos, c_p_score, c_p_name, n_p_pos, n_p_score, n_p_name, num_branches):
    for step_count in step_counts:
        new_c_p_pos = (c_p_pos + step_count) % 10
        new_c_p_score = c_p_score + new_c_p_pos + 1
        if new_c_p_score >= 21:
            win_counts[c_p_name] += num_branches*step_counts[step_count]
        else:
            do_rounds(win_counts, step_counts, n_p_pos, n_p_score, n_p_name, new_c_p_pos, new_c_p_score, c_p_name, num_branches*step_counts[step_count])


win_counts = {'p1': 0, 'p2': 0}
do_rounds(win_counts, step_counts, players[0]._pos, 0, "p1", players[1]._pos, 0, "p2", 1)

print(win_counts)
