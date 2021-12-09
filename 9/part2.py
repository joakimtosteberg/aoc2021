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

def explore_basin(points, heightmap, basin):
    new_points = []
    for point in points:
        for step in [(0,1),(0,-1),(1,0),(-1,0)]:
            adjacent_point = (point[0]+step[0],point[1]+step[1])
            if adjacent_point in basin:
                continue
            if not adjacent_point in heightmap:
                continue
            if heightmap[adjacent_point] >= heightmap[point] and heightmap[adjacent_point] != 9:
                new_points.append(adjacent_point)
                basin[adjacent_point] = True
    if new_points:
        return explore_basin(new_points, heightmap, basin)
    else:
        return basin
    
def get_basin_size(point, heightmap):
    basin = {}
    basin[point] = True
    basin = explore_basin([point], heightmap, basin)
    return len(basin)

basin_sizes = []
for y in range(0,map_height):
    for x in range(0,map_width):
        if is_low_point((x,y), heightmap):
            basin_sizes.append(get_basin_size((x,y), heightmap))

basin_sizes.sort(reverse=True)
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
