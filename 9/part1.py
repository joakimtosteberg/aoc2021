import sys

heightmap = {}
map_width = 0
with open(sys.argv[1]) as f:
    x = 0
    map_height = 0
    for line in f:
        for height in line.strip():
            heightmap[(x,map_height)] = int(height)
            x = x + 1
        map_height = map_height + 1
        map_width = x
        x = 0

def is_low_point(point, heightmap):
    for step in [(0,1),(0,-1),(1,0),(-1,0)]:
        adjacent_point = (point[0]+step[0],point[1]+step[1])
        if adjacent_point in heightmap:
            if heightmap[adjacent_point] <= heightmap[point]:
                break
    else:
        return True

def get_risk_level(point, heightmap):
    return heightmap[point] + 1

risk_level = 0
for y in range(0,map_height):
    for x in range(0,map_width):
        if is_low_point((x,y), heightmap):
            risk_level = risk_level + get_risk_level((x,y), heightmap)

print(risk_level)
