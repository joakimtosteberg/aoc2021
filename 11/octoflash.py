import copy
import queue
import sys

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashing = False

    def increase_energy(self):
        self.energy = self.energy + 1

    def is_flashing(self):
        if self.energy > 9 and not self.flashing:
            self.flashing = True
            return True
        return False

    def reset(self):
        self.flashing = False
        if self.energy > 9:
            self.energy = 0

    def __str__(self):
        return f"{self.energy}:{self.flashing}"


initial_grid = {}
x = 0
y = 0
with open(sys.argv[1]) as f:
    for line in f:
        x = 0
        for energy in line.strip():
            initial_grid[(x,y)] = Octopus(int(energy))
            x = x + 1
        y = y + 1

width = x
height = y

def spread_flash(grid, width, height, flash):
    steps = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0)]
    flashes = []
    for step in steps:
        pos = (flash[0] + step[0],
               flash[1] + step[1])
        if pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height:
            continue
        grid[pos].increase_energy()
        if grid[pos].is_flashing():
            flashes.append(pos)
    return flashes

def step(grid, width, height):
    flashes = []
    num_flashes = 0
    for y in range(0,height):
        for x in range(0,width):
            grid[(x,y)].increase_energy()
            if grid[(x,y)].is_flashing():
                flashes.append((x,y))
    num_flashes = num_flashes + len(flashes)
    while flashes:
        new_flashes = []
        for flash in flashes:
            new_flashes = new_flashes + spread_flash(grid, width, height, flash)
        flashes = new_flashes
        num_flashes = num_flashes + len(flashes)

    for y in range(0,height):
        for x in range(0,width):
            grid[(x,y)].reset()

    return num_flashes

def print_grid(grid, width, height):
    for y in range(0,height):
        for x in range(0,width):
            print(grid[(x,y)].energy, end='')
        print()

num_flashes = 0
num_steps = 100
grid = copy.deepcopy(initial_grid)
for i in range(0,num_steps):
    num_flashes = num_flashes + step(grid, width, height)

print(f"{num_flashes} flashes after {num_steps} steps")


iteration = 0
grid = copy.deepcopy(initial_grid)
while True:
    num_flashes = step(grid, width, height)
    iteration = iteration + 1
    if num_flashes == width*height:
        break

print(f"Simultaneous flashing after {iteration} steps")
