import queue
import sys

open_chunks = queue.LifoQueue()

lookup = {'(': ')',
          '[': ']',
          '{': '}',
          '<': '>'}

points = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}


total_points = 0
with open(sys.argv[1]) as f:
    for line in f:
        for c in line.strip():
            if c in lookup:
                open_chunks.put(c)
            else:
                opener = open_chunks.get()
                if lookup[opener] != c:
                    total_points = total_points + points[c]
                    break
        
print(total_points)
