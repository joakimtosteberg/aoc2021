import sys

positions = {}
max_position = 0
with open(sys.argv[1]) as f:
    for value in f.readline().split(','):
        if int(value) in positions:
            positions[int(value)] = positions[int(value)] + 1
        else:
            positions[int(value)] = 1
            max_position = max(max_position, int(value))

def simple_cost(distance):
    return distance

def real_cost(distance):
    return int(((1+distance)*distance)/2)

def get_cost(positions, pos, cost_func):
    cost = 0
    for item in positions.items():
        cost = cost + cost_func(abs(item[0]-pos)) * item[1]
    return cost

def get_best_cost(positions, cost_func):
    best_cost = 0
    best_pos = -1
    for pos in range(0,max_position):
        cost = get_cost(positions, pos, cost_func)
        if cost < best_cost or best_pos == -1:
            best_cost = cost
            best_pos = pos
    return (best_cost, best_pos)

best_cost, best_pos = get_best_cost(positions, simple_cost)
print(f"best cost is {best_cost} as position {best_pos}")

best_cost, best_pos = get_best_cost(positions, real_cost)
print(f"best cost is {best_cost} as position {best_pos}")
