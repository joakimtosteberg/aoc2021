import copy
import sys

paths = []
cavern = {}
visited = {}        

with open(sys.argv[1]) as f:
    for line in f:
        path = line.strip().split('-')
        if path[0] not in cavern:
            cavern[path[0]] = [path[1]]
        else:
            cavern[path[0]].append(path[1])

        if path[1] not in cavern:
            cavern[path[1]] = [path[0]]
        else:
            cavern[path[1]].append(path[0])
        visited[path[0]] = 0
        visited[path[1]] = 0

def allow_visit(cave, visited, allow_double):
    if not visited[cave] or cave.isupper() or cave == 'end':
        return (True,allow_double)

    if visited[cave] == 1 and allow_double:
        return (True,False)

    return (False,allow_double)

def find_paths(cavern, position, path, paths, visited, allow_double):
    if position == 'end':
        paths.append(path)
        return

    if position not in cavern:
        return

    for cave in cavern[position]:

        ok_to_visit, new_allow_double = allow_visit(cave, visited, allow_double)
        if ok_to_visit:
            visited[cave] = visited[cave] + 1
            find_paths(cavern, cave, path + [cave], paths, visited, new_allow_double)
            visited[cave] = visited[cave] - 1

visited['start'] = 2
find_paths(cavern, 'start', ['start'], paths, copy.deepcopy(visited), False)
print(f"{len(paths)} paths found for part1")
paths = []
find_paths(cavern, 'start', ['start'], paths, copy.deepcopy(visited), True)
print(f"{len(paths)} paths found for part2")
