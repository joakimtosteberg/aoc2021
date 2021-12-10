import queue
import sys

lookup = {'(': ')',
          '[': ']',
          '{': '}',
          '<': '>'}

points = {'(': 1,
          '[': 2,
          '{': 3,
          '<': 4}

def score_incomplete_chunk(open_chunks):
    score = 0
    while not open_chunks.empty():
        opener = open_chunks.get()
        score = score * 5 + points[opener]
    return score

scores = []
with open(sys.argv[1]) as f:
    for line in f:
        open_chunks = queue.LifoQueue()
        for c in line.strip():
            if c in lookup:
                open_chunks.put(c)
            else:
                opener = open_chunks.get()
                if lookup[opener] != c:
                    break
        else:
            scores.append(score_incomplete_chunk(open_chunks))

print(sorted(scores)[int((len(scores)-1)/2)])
