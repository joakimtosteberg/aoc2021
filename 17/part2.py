import sys

def get_range(data):
    speed_range = data.split('=')[1].split('..')
    return (int(speed_range[0]), int(speed_range[1]))

with open(sys.argv[1]) as f:
    data = f.readline().strip()[13:].split(', ')
    x_range = get_range(data[0])
    y_range = get_range(data[1])

def in_range(pos, target_range):
    return (pos >= target_range[0] and
            pos <= target_range[1])

def simulate_x_position(speed, x_range):
    steps = 0
    x_pos = 0
    while speed > 0:
        x_pos = x_pos + speed
        speed = speed - 1
        steps = steps + 1
        if in_range(x_pos, x_range):
            return (steps,x_pos)
    return None

def simulate_position(initial_x_speed, x_start, min_steps, y_range, negative):
    x_pos = x_start
    y_speed = 0
    if negative:
        y_speed = y_speed - 1
    ok_speeds = []
    while True:
        x_speed = initial_x_speed
        x_pos = x_start
        steps = min_steps
        
        while True:
            y_pos = int((2*y_speed*steps - steps*steps + steps)/2)
            if in_range(y_pos, y_range):
                ok_speeds.append((x_speed,y_speed))

            if y_pos < y_range[0]:
                break

            if (x_speed - steps) > 0:
                x_pos = x_pos + (x_speed - steps)
                if not in_range(x_pos, x_range):
                    break

            steps = steps + 1

        if negative:
            y_speed = y_speed - 1
            if y_speed < -1000:
                break
        else:
            y_speed = y_speed + 1
            if y_speed > 1000:
                break
    return ok_speeds

x_speed = 1
possible_steps = []

while x_speed <= x_range[1]:
    steps = simulate_x_position(x_speed, x_range)
    if steps:
        possible_steps.append((x_speed,steps[0], steps[1]))
    x_speed = x_speed + 1
        
best_y_speed = 0
best_speed_tuple = None
ok_speeds = []
for x_step in possible_steps:
    x_speed = x_step[0]
    min_steps = x_step[1]
    x_start = x_step[2]
    ok_speeds = ok_speeds + simulate_position(x_speed, x_start, min_steps, y_range, False)
    ok_speeds = ok_speeds + simulate_position(x_speed, x_start, min_steps, y_range, True)

print(len(set(ok_speeds)))

