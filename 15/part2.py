import sys

cave = {}
risk_map = {}

width = 0
height = 0
with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for risk in line.strip():
            cave[(x,y)] = int(risk)
            risk_map[(x,y)] = -1
            x = x + 1
        width = x
        y = y + 1
    height = y


for y in range(0,height*5):
    for x in range(0,width*5):
        if x < width and y < height:
            continue
        if y < height:
            read_x = x-width
            read_y = y
        else:
            read_x = x
            read_y = y - height
        risk = cave[read_x,read_y] + 1
        if risk > 9:
            risk = 1
        cave[(x,y)] = risk
        risk_map[(x,y)] = -1

risk_map[(0,0)] = 0
width = width*5
height = height * 5

def explore(positions, cave, risk_map):
    steps = [(0,1),(0,-1),(1,0),(-1,0)]
    next_positions = []
    for pos in positions:
        for step in steps:
            next_pos = (pos[0]+step[0],pos[1]+step[1])
            if ((next_pos[0] < 0) or (next_pos[0] >= width) or
                (next_pos[1] < 0) or (next_pos[1] >= height)):
                continue
            next_pos_risk = risk_map[pos] + cave[next_pos]
            if (risk_map[next_pos] == -1) or (next_pos_risk < risk_map[next_pos]):
                risk_map[next_pos] = next_pos_risk
                next_positions.append(next_pos)
    return  set(next_positions)


def print_riskmap(risk_map, widht, height):
    for y in range(0,height):
        for x in range(0,width):
            print(risk_map[(x,y)], end=' ')
        print()
positions = {(0,0)}
while True:
    positions = explore(positions, cave, risk_map)
    if not positions:
        break
#print_riskmap(risk_map, width, height)
print(risk_map[(width-1,height-1)])
