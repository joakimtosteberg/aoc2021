import sys

grid = {}
folds = []

with open(sys.argv[1]) as f:
    read_points = True
    for line in f:
        data = line.strip()
        if not data:
            read_points = False
            continue
        if read_points:
            data = data.split(',')
            grid[(int(data[0]), int(data[1]))] = 'x'

        else:
            data = data[11:].split('=')
            folds.append((data[0], int(data[1])))

def print_grid(grid):
    max_x = 0
    max_y = 0 
    for item in grid:
        max_x = max(max_x,item[0])
        max_y = max(max_y,item[1])

    for y in range(0,max_y+1):
        for x in range(0,max_x+1):
            if (x,y) in grid:
                print('#', end='')
            else:
                print('.', end='')
        print('')

first_fold = True
for fold in folds:
    next_grid = {}
    fold_axis = 0 if fold[0] == 'x' else 1
    for item in grid:
        if item[fold_axis] < fold[1]:
            next_grid[item] = 'x'
        if item[fold_axis] > fold[1]:
            if fold_axis == 0:
                next_grid[(2*fold[1]-item[0],item[1])] = 'x'
            else:
                next_grid[(item[0],2*fold[1]-item[1])] = 'x'
    grid = next_grid
    if first_fold:
        print(len(grid))
        first_fold = False
print_grid(grid)
